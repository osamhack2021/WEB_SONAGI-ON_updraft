from .models import Diary
from rest_framework import serializers
from .models import emotion_choices

class DiaryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['title', 'content', 'emotion']

class DiaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ['id', 'title', 'content', 'emotion', 'write_date']

class DiarySearchSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(label='검색 시작일')
    end_date = serializers.DateField(label='검색 종료일')
    search = serializers.CharField(label='검색어', required=False, allow_blank=True)
    emotion = serializers.ChoiceField(label='감정', choices=(('', '모두'),)+emotion_choices)

    class Meta:
        model = Diary
        fields = ["start_date", "end_date", "search", "emotion"]