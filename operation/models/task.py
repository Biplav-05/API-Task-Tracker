from django.db import models
from operation.models.directory import Todo

class Task(models.Model):
    name = models.CharField(max_length=100)
    assignee = models.EmailField(blank=True, null=True)
    priority = models.CharField(max_length=100)  # Add max_length parameter
    due_date = models.DateTimeField(auto_now=True)
    todo = models.ForeignKey(Todo, on_delete=models.DO_NOTHING)

class SubTask(models.Model):
    name = models.CharField(max_length=100)
    assignee = models.EmailField(blank=True, null=True)
    priority = models.CharField(max_length=100)  # Add max_length parameter
    due_date = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
