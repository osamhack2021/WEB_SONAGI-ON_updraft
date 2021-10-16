from .models import Contest
from rest_framework import serializers
from rest_framework.request import Request

class ContestListSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(use_url=True)

    class Meta:
        model = Contest
        fields = '__all__'