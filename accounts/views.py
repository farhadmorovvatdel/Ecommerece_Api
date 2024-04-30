from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.views import APIView
from .Serializer import RegisterSerializer,Loginserializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class RegisterView(APIView):
    def post(self, request:Request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(phone_number=serializer.data['phone_number'])
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self,request:Request):
        serializer = Loginserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        password = serializer.validated_data['password']
        user = authenticate(request,phone_number=phone_number,password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            data={
                "error":"this user dosent exists"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

       