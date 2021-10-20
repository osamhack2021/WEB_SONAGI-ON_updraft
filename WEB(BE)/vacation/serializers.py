from .models import Vacation
from rest_framework import serializers

class VactionSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Vacation
        fields = '__all__'
        extra_kwargs = {"email": {"read_only": True}}