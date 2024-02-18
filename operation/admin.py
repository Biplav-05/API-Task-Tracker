from django.contrib import admin
from .models.work_space import WorkSpace
from .models.space import Space
from .models.directory import Directory, SubDirectory, List, Todo
from .models.task import Task, SubTask

# Register your models here.

admin.site.register(WorkSpace)
admin.site.register(Space)
admin.site.register(Directory)
admin.site.register(SubDirectory)
admin.site.register(List)
admin.site.register(Todo)
admin.site.register(Task)
admin.site.register(SubTask)