from django.urls import path
from operation.views import Test

urlpatterns = [
    path('', Test.as_view(), name='google-access-token-generate'),
]   