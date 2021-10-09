from django.db import models

# Create your models here.

major_choices = (
    ('army', "육군"),
    ('navy', "해군"),
    ('air', "공군"),
    ('marine', '해병대'),
)

type_choices = (
    ('soldier', '용사'),
    ('nco', '부사관'),
    ('officer', '장교'),
)

class UserSetting(models.Model):
    email = models.EmailField(verbose_name="유저 이메일", max_length=255, unique=True, null=False)
    # todo : 회원가입 시 아래 내용들 다 랜덤으로 채워버린 다음에 바로 초기 세팅 화면으로 넘겨서 세팅 시키거나
    #        회원가입 전에 아래 내용들을 다 받자
    nickname = models.CharField(verbose_name="닉네임", max_length=20, null=False, unique=True)
    major = models.CharField(verbose_name="군 구분", max_length=10, choices=major_choices, null=False)
    type = models.CharField(verbose_name="복무 구분", max_length=10, choices=type_choices, null=False)
    enlisted_date = models.DateField(verbose_name="입대일(임관일)", null=False)
    delisted_date = models.DateField(verbose_name="전역일", null=False)
    promotion1_date = models.DateField(verbose_name="일병(중사,중위) 진급일", null=False)
    promotion2_date = models.DateField(verbose_name="상병(상사,대위) 진급일", null=False)
    promotion3_date = models.DateField(verbose_name="병장(소령) 진급일", null=False)