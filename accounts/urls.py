from django.urls import path
from accounts.views import email_login_signup_view 
from accounts.views import google_access_token_generator_view
from accounts.views import google_login_view

urlpatterns = [
    path('login', google_access_token_generator_view.google_login, name='google-access-token-generate'),
    path('login/google', google_login_view.UserGoogleLoginView.as_view(), name='google-access-token-generate'),
    path('google/callback',google_access_token_generator_view.google_callback, name='google-callback'),
    path('email-signup', email_login_signup_view.UserEmailSignUpView.as_view(), name='email-signup-view'),
    path('email-login', email_login_signup_view.UserEmailSignInView.as_view(), name='sign-in-view'),
]   