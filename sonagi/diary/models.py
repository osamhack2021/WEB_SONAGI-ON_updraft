from django.db import models

# Create your models here.

emotion_choices = (
    ('excited', "excited"),
    ('cool', "cool"),
    ('neutral', "neutral"),
    ('confused', 'confused'),
    ('angry', 'angry'),
    ('sad', 'sad'),
    ('sick', 'sick'),
    ('cry', 'cry'),
    ('dead', 'dead'),
)

class Diary(models.Model):
    email = models.ForeignKey("user.User", related_name="diary", to_field="email", on_delete=models.CASCADE, db_column="email")
    title = models.CharField(verbose_name="한줄평", max_length=100, null=False)
    content = models.CharField(verbose_name="내용", max_length=2000, null=True)
    emotion = models.CharField(verbose_name="감정", max_length=10, choices=emotion_choices, null=False)
    write_date = models.DateField(verbose_name="작성 일자", auto_now_add=True)
    rewrite_date = models.DateField(verbose_name="최종 수정 일자", auto_now=True)