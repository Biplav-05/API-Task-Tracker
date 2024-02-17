from django.urls import path
from accounts.views import email_login_signup_view 

urlpatterns = [
    path('email-signup/', email_login_signup_view.UserEmailSignUpView.as_view(), name='email-signup-view'),
    path('email-login/', email_login_signup_view.UserEmailSignInView.as_view(), name='sign-in-view'),
    
    
]   