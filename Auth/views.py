from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user.username,
                }
            )
        else:
            return Response(
                {"detail": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

class SignupView(APIView):

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'Please provide all required fields'}, status=400)

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return Response({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class ResetPasswordView(APIView):

    def post(self, request, username):
        new_password = request.data.get('new_password')
        if not new_password:
            return Response({"detail": "New password not provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.password = make_password(new_password)
        user.save()

        return Response({"detail": "Password reset successful"}, status=status.HTTP_200_OK)