from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="- -", null=True, blank=True)
    description = models.TextField(blank=True, default="- - -")
    profile_pic = models.ImageField(default="profile_default.jpg", blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        user_str = str(self.user)
        return user_str
