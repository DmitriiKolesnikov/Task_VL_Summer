from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)


class FriendRequest(models.Model):
    source_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="source_user")
    dest_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dest_user")

    class StatusRequest(models.IntegerChoices):
        UNANSWERED = 1
        ACCEPTED = 2
        DECLAINED = 3
    status = models.IntegerField(choices=StatusRequest.choices, default=StatusRequest.UNANSWERED, null=True)



