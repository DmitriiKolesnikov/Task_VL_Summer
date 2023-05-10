from rest_framework import serializers

from friends.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FriendRequestSerializer(serializers.ModelSerializer):
    source_user = serializers.CharField(read_only=True)
    dist_user = serializers.CharField(read_only=True)

    class Meta:
        model = FriendRequest
        fields = "__all__"
