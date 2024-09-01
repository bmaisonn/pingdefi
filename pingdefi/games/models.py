from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

class UsersGame(models.Model):
    time = models.DateTimeField
    user1 = models.ForeignKey(User, related_name="user1", on_delete=models.SET_NULL, null=True)
    user2 = models.ForeignKey(User, related_name="user2", on_delete=models.SET_NULL, null=True)
    winner = models.ForeignKey(User, related_name="winner", on_delete=models.SET_NULL, null=True)
    score = models.JSONField()

