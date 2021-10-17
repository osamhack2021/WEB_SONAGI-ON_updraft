from .models import UserSetting
from rest_framework import serializers

# https://brownbears.tistory.com/71 partial update
class UserSettingSerializer(serializers.ModelSerializer):
    profile = serializers.ImageField(use_url=True)

    class Meta:
        model = UserSetting
        fields = ["email", 
                  "nickname",
                  "profile", 
                  "major", 
                  "type", 
                  "enlisted_date", 
                  "delisted_date", 
                  "promotion1_date", 
                  "promotion2_date", 
                  "promotion3_date"]
        extra_kwargs = {"email": {"read_only": True}}
    def validate_nickname(self, val):
        if len(val) < 2 or len(val) > 15 :
            raise serializers.ValidationError({'nickname' : '닉네임은 2자 이상 15자 이하여야 합니다.'})
        return val
        