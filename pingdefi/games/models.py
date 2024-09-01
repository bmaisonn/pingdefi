from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

class UsersGame(models.Model):
    time = models.DateTimeField
    user1 = models.ForeignKey(User)
    user2 = models.ForeignKey(User)
    score = models.JSONField()
    winner = models.ForeignKey(User)

