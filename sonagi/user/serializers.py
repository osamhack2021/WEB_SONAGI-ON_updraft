from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email"]


# 회원가입
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='비밀번호 확인')

    class Meta:
        model = User
        fields = ("id", "email", "password", "password2",)
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, request):
        user = User.objects.create_user(
            self.validated_data["email"], self.validated_data["password"]
        )
        return user
    
    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError({'password' : '패스워드가 일치하지 않습니다.'})
        return data # must return validated values