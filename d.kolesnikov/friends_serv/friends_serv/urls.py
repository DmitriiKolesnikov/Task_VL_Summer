from django.urls import path
from friends import views

from friends.views import UserViewsetList, FriendRequestViewsetList, FriendshipViewsetList

urlpatterns = [
    path('user/', UserViewsetList.as_view({'post': 'post'}), name='user'),
    path('user/<int:pk>', UserViewsetList.as_view({'get': 'retrieve'}), name='user_get'),
    path('friend_request/', FriendRequestViewsetList.as_view({'post': 'post'}), name='friend_request'),
    path('friend_request/<int:pk>', FriendRequestViewsetList.as_view({'put': 'change_status'}), name='friend_request_change_status'),
    path('friendship/<int:pk>', FriendshipViewsetList.as_view({'get': 'get'}), name="friendship_list"),
    path('register/', views.register, name='register'),
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
    path('accept_friend_request/<int:user_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:user_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('incoming_friend_requests/', views.incoming_friend_requests, name='incoming_friend_requests'),
    path('outgoing_friend_requests/', views.outgoing_friend_requests, name='outgoing_friend_requests'),
    path('friend_list/', views.friend_list, name='friend_list'),
    path('friendship_status/<int:user_id>/', views.friendship_status, name='friendship_status'),
    path('remove_friend/<int:user_id>/', views.remove_friend, name='remove_friend'),
]


