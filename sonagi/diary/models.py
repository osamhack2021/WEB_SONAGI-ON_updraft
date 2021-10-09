from django.db import models

# Create your models here.

emotion_choices = (
    ('G', "좋음"),
    ('N', "보통"),
    ('B', "별로"),
    ('C', '슬픔'),
    ('S', '놀람')
)

class Diary(models.Model):
    email = models.EmailField(verbose_name="작성자 이메일")
    title = models.CharField(verbose_name="한줄평", max_length=100, null=False)
    content = models.CharField(verbose_name="내용", max_length=2000, null=True)
    emotion = models.CharField(verbose_name="감정", max_length=1, choices=emotion_choices, null=False)
    write_date = models.DateField(verbose_name="작성 일자", auto_now_add=True)
    rewrite_date = models.DateField(verbose_name="최종 수정 일자", auto_now=True)