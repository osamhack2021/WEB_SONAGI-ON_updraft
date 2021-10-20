from django.db import models
from django.utils import timezone

type_choices = (
    (0, "포상"),
    (1, "보상"),
    (2, "위로"),
    (3, '청원'),
    (4, '정기'),
    (5, '외박'),
    (6, '기타'),
)

# Create your models here.

class Vacation(models.Model):
    email = models.ForeignKey("user.User", related_name="vacation", to_field="email", on_delete=models.CASCADE, db_column="email")
    name = models.CharField(verbose_name="이름", max_length=20, null=False)
    type = models.IntegerField(verbose_name="타입", choices=type_choices, null=False)
    day = models.DateField(verbose_name="받은 날짜", default=timezone.now)
    termS = models.IntegerField(verbose_name="받은 일수", null=False)
    usedS = models.IntegerField(verbose_name="사용 일수", null=False)