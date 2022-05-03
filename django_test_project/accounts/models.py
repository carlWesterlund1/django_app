from django.contrib.auth.models import User
from django.db import models
"""
- User objects have the following fields:

username
first_name, last_name
email, password
groups
user_permissions
is_staff, is_active, is_superuser
last_login, date_joined
"""
class UserProfile(User):
    desription = models.TextField(blank=True)
    profile_pic = models.ImageField(default="default.png", blank=True)
