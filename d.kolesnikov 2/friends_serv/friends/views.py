from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q

from rest_framework import status
from rest_framework import viewsets

from .models import User, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer

class UserViewsetList(viewsets.ViewSet):
    def retrieve(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return JsonResponse({'user': UserSerializer(user).data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FriendRequestViewsetList(viewsets.ViewSet):
    def post(self, request):
        if 'source_user' not in request.data:
            return JsonResponse({'errors': 'field "source_user" is required'}, status=status.HTTP_400_BAD_REQUEST)
        if 'dest_user' not in request.data:
            return JsonResponse({'errors': 'field "dest_user" is required'}, status=status.HTTP_400_BAD_REQUEST)
        source_user = get_object_or_404(User, id=int(request.data['source_user']))
        dest_user = get_object_or_404(User, id=int(request.data['dest_user']))
        friend_request = FriendRequest.objects.filter(source_user=source_user, dest_user=dest_user)
        if len(friend_request) > 0:
            return JsonResponse({'errors': 'The friend request exists'}, status=status.HTTP_400_BAD_REQUEST)
        friend_request_reverse = FriendRequest.objects.filter(dest_user=source_user, source_user=dest_user, status=FriendRequest.StatusRequest.UNANSWERED)
        if len(friend_request_reverse) > 0:
            friend_request = friend_request_reverse[0]
            friend_request.status = FriendRequest.StatusRequest.ACCEPTED
            friend_request.save()
            serializer = FriendRequestSerializer(friend_request)
            return JsonResponse({'friend_request': serializer.data}, status=status.HTTP_201_CREATED)
        friend_request = FriendRequest.objects.create(source_user=source_user, dest_user=dest_user)
        serializer = FriendRequestSerializer(friend_request)
        return JsonResponse({'friend_request': serializer.data}, status=status.HTTP_201_CREATED)

    def change_status(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, id=pk, status=FriendRequest.StatusRequest.UNANSWERED)
        if 'status' not in request.data:
            return JsonResponse({'errors': 'field "status" is required'}, status=status.HTTP_400_BAD_REQUEST)
        status = int(request.data['status'])
        if status == FriendRequest.StatusRequest.ACCEPTED:
            friend_request.status = FriendRequest.StatusRequest.ACCEPTED
        elif status == FriendRequest.StatusRequest.DECLINED:
            friend_request.status = FriendRequest.StatusRequest.DECLINED
        friend_request.save()
        serializer = FriendRequestSerializer(friend_request)
        return JsonResponse({'friend_request': serializer.data}, status=status.HTTP_201_CREATED)

class FriendshipViewsetList(viewsets.ViewSet):
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        incoming_requests = FriendRequest.objects.filter(source_user=user, status=FriendRequest.StatusRequest.UNANSWERED).all()
        outgoing_requests = FriendRequest.objects.filter(dest_user=user, status=FriendRequest.StatusRequest.UNANSWERED).all()
        return JsonResponse({'user': {'incoming': FriendRequestSerializer(incoming_requests, many=True).data, 'outgoing': FriendRequestSerializer(outgoing_requests, many=True).data}})

    def list(self, request, pk):
        user = get_object_or_404(User, id=pk)
        friends = FriendRequest.objects.filter(Q(source_user=user) | Q(dest_user=user), status=FriendRequest.StatusRequest.ACCEPTED).all()
        return JsonResponse({'user': {'friends': FriendRequestSerializer(friends, many=True).data}})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        return JsonResponse({'status': 'success'})
    return render(request, 'register.html')


def send_friend_request(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    request.user.friend_requests.add(friend)
    return JsonResponse({'status': 'success'})


def accept_friend_request(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    request.user.friends.add(friend)
    request.user.friend_requests.remove(friend)
    friend.friends.add(request.user)
    return JsonResponse({'status': 'success'})


def reject_friend_request(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    request.user.friend_requests.remove(friend)
    return JsonResponse({'status': 'success'})


def incoming_friend_requests(request):
    friend_requests = request.user.friend_requests.all()
    return render(request, 'friend_requests.html', {'friend_requests': friend_requests})


def outgoing_friend_requests(request):
    friend_requests = request.user.requested_friends.all()
    return render(request, 'friend_requests.html', {'friend_requests': friend_requests})


def friend_list(request):
    friends = request.user.friends.all()
    return render(request, 'friend_list.html', {'friends': friends})


def friendship_status(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    if friend in request.user.friends.all():
        status = 'Friends'
    elif friend in request.user.friend_requests.all():
        status = 'Request Sent'
    elif request.user in friend.friend_requests.all():
        status = 'Request Received'
    else:
        status = 'Not Connected'
    return JsonResponse({'status': status})


def remove_friend(request, user_id):
    friend = get_object_or_404(User, id=user_id)
    request.user.friends.remove(friend)
    friend.friends.remove(request.user)
    return JsonResponse({'status': 'success'})
