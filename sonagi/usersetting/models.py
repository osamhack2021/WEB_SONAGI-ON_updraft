from django.db import models
import os
import uuid
from django.utils.deconstruct import deconstructible

# Create your models here.

@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        extension = os.path.splitext(filename)[1]
        return self.path % (uuid.uuid4(), extension)

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
    email = models.ForeignKey("user.User", related_name="setting", to_field="email", on_delete=models.CASCADE, db_column="email")
    nickname = models.CharField(verbose_name="닉네임", max_length=20, null=False, unique=True)
    profile = models.ImageField(verbose_name="프로필 이미지", upload_to=RandomFileName("profile"), blank=True)
    major = models.CharField(verbose_name="군 구분", max_length=10, choices=major_choices, null=False)
    type = models.CharField(verbose_name="복무 구분", max_length=10, choices=type_choices, null=False)
    enlisted_date = models.DateField(verbose_name="입대일(임관일)", null=False)
    delisted_date = models.DateField(verbose_name="전역일", null=False)
    promotion1_date = models.DateField(verbose_name="일병(중사,중위) 진급일", null=False)
    promotion2_date = models.DateField(verbose_name="상병(상사,대위) 진급일", null=False)
    promotion3_date = models.DateField(verbose_name="병장(소령) 진급일", null=False)