from django.urls import path
from tasks.views import PersonTestView

urlpatterns = [
    path('', PersonTestView.as_view(), name='test person'),
]   