from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class CustomUserAccount(AbstractUser):
    # username=None
    email=models.EmailField(unique=True)
    avtar=models.CharField(null=True, blank=True)
    user_bio=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []
    objects=UserManager()