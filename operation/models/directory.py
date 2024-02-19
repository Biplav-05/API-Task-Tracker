from django.db import models
from operation.models.space import Space
from django.utils import timezone

class Directory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    space = models.ForeignKey(Space, on_delete=models.DO_NOTHING)

class SubDirectory(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    directory = models.ForeignKey(Directory, on_delete=models.DO_NOTHING)

class List(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    sub_directory = models.ForeignKey(SubDirectory, on_delete=models.DO_NOTHING)

class Todo(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    list = models.ForeignKey(List, on_delete=models.DO_NOTHING)

    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(Todo, self).save(*args, **kwargs)
