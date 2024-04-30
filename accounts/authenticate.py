from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import User
User=get_user_model()
class PhoneBackend(BaseBackend):
    def authenticate(self, request, phone_number=None, password=None):
        user = User.objects.get(phone_number=phone_number)
        if user.check_password(password):
                return user
       
    # def get_user(self, user_id: int):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None