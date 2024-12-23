from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    related_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} {self.action}"
