from .models import UserSetting
from rest_framework import serializers

# https://brownbears.tistory.com/71 partial update
class UserSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSetting
        fields = ["email", "nickname", "major", "type", "enlisted_date", "delisted_date", "promotion1_date", "promotion2_date", "promotion3_date"]
        extra_kwargs = {"email": {"read_only": True}}
    def validate_nickname(val):
        if len(val) < 4 or len(val) > 15 :
            raise serializers.ValidationError({'nickname' : '닉네임은 4자 이상 15자 이하여야 합니다.'})
        return val
        