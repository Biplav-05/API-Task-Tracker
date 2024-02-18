from django.urls import path
from .views import work_space_view

urlpatterns = [
    path('workspace', work_space_view.WorkSpaceListView.as_view(), name='workspace-list-view'),
]   