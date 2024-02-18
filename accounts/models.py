from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import gettext_lazy as _

class CustomUserAccount(AbstractUser):
    email=models.EmailField(unique=True)
    user_bio=models.CharField(max_length=100)
    display_name = models.CharField(_("display name"), max_length=150, null=True, blank=True)
    avatar = models.CharField(_("avatar"), max_length=5000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
    objects=UserManager()