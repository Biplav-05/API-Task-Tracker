from django.db import models
from operation.models.work_space import WorkSpace

class Space(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    work_space=models.ForeignKey(WorkSpace, on_delete=models.DO_NOTHING)