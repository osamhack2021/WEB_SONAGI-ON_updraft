from django.db import models

status_choice = (
    ('before_register', '접수 전'),
    ('register', '접수 중'),
    ('before_progress', '진행 전'),
    ('progress', '진행 중'),
    ('end', '종료'),
)

# Create your models here.
class Contest(models.Model):
    poster = models.ImageField(verbose_name="포스터", upload_to="contest/", blank=True)
    title = models.CharField(verbose_name="행사제목", max_length=100, null=True)
    content = models.TextField(verbose_name="행사내용",  null=True)
    host = models.CharField(verbose_name="주최", max_length=50, null=True)
    organizer = models.CharField(verbose_name="주관", max_length=50, null=True)
    qualification = models.CharField(verbose_name="참가자격", max_length=50, null=True)
    reward_amount = models.CharField(verbose_name="시상금", max_length=50, null=True)
    site = models.CharField(verbose_name="홈페이지", max_length=50, null=True)
    start_date = models.DateField(verbose_name="접수기간(시작)")
    end_date =models.DateField(verbose_name="접수기간(종료)")
    contest_status = models.CharField(verbose_name="상태", max_length=20, choices=status_choice, null=False)