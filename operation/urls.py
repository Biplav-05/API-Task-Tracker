from django.urls import path

from .views import work_space_view, space_view

urlpatterns = [
    path('workspace', work_space_view.WorkSpaceListView.as_view(), name='workspace-list-view'),
    path('<int:work_space_id>/workspace', work_space_view.WorkSpaceDetailView.as_view(), name='workspace-detail-view'),
    path('<int:work_space_id>/space', space_view.SpaceListView.as_view(), name='space-detail-view'),
    path('<int:work_space_id>/space/<int:space_id>', space_view.SpaceDetailView.as_view(), name='space-detail-view'),
]   