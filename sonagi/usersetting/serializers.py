from .models import UserSetting
from rest_framework import serializers

# https://brownbears.tistory.com/71 partial update
class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = '__all__'