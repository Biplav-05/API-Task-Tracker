from django.db import models
from accounts.models import CustomUserAccount

class WorkSpace(models.Model):
    name=models.TextField(max_length=250, blank=False, null=False)
    description=models.TextField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(CustomUserAccount, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)