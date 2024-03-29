from rest_framework.response import Response
from accounts.serializers.email_login_signup_serializer import EmailSignInSerializer, EmailSignUpSerializer
from accounts.models import CustomUserAccount
from rest_framework import status
from rest_framework.views import APIView
from accounts.utils import generate_access_token, generate_refresh_token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


class UserEmailSignUpView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Creates new user signing up with email.
        """
        serializer = EmailSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Check if user with the provided email already exists
        existing_user = CustomUserAccount.objects.filter(email=request.data['email']).exists()
        if existing_user:
            return Response("User with that email already exists", status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response("New user created", status=status.HTTP_201_CREATED)
    
class UserEmailSignInView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Logs in user with email and password
        """
        serializer = EmailSignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)

        if user:
            access_token = generate_access_token(user)
            refresh_token = generate_refresh_token(user)
            data = {'access_token': access_token, 'refresh_token': refresh_token}
            response = Response(data=data, status=status.HTTP_202_ACCEPTED)
            response.set_cookie(key="refreshtoken", value=refresh_token, httponly=True)
            return response
        
        return Response("Invalid Username or Password", status=status.HTTP_400_BAD_REQUEST)
