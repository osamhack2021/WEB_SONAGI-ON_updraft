from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]


# 회원가입
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='비밀번호 확인')

    class Meta:
        model = User
        fields = ("id", "username", "email", "nickname", "password", "password2",)
        extra_kwargs = {"password": {"write_only": True}}

    def save(self, request):
        user = User.objects.create_user(
            self.validated_data["username"], self.validated_data["email"], self.validated_data["nickname"], self.validated_data["password"]
        )
        return user
    
    def validate(self, data):
        password1 = data.get('password')
        password2 = data.get('password2')
        if password1 != password2:
            raise serializers.ValidationError({'password' : '패스워드가 일치하지 않습니다.'})
        return data # must return validated values
    
    def validate_username(self, value):
        if len(value) > 15:
            raise serializers.ValidationError({'username' : '아이디는 15자 내의 영숫자로만 이루어져 있어야 합니다.'})
        return value