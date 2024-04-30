from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['phone_number']

class Loginserializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField()    
    
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'password')

    def validate_password(self, value):
        return make_password(value)   