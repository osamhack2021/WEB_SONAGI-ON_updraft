# Generated by Django 3.2.7 on 2021-10-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='유저 이메일')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='닉네임')),
                ('major', models.CharField(choices=[('army', '육군'), ('navy', '해군'), ('air', '공군'), ('marine', '해병대')], max_length=10, verbose_name='군 구분')),
                ('type', models.CharField(choices=[('soldier', '용사'), ('nco', '부사관'), ('officer', '장교')], max_length=10, verbose_name='복무 구분')),
                ('enlisted_date', models.DateField(verbose_name='입대일(임관일)')),
                ('delisted_date', models.DateField(verbose_name='전역일')),
                ('promotion1_date', models.DateField(verbose_name='일병(중사,중위) 진급일')),
                ('promotion2_date', models.DateField(verbose_name='상병(상사,대위) 진급일')),
                ('promotion3_date', models.DateField(verbose_name='병장(소령) 진급일')),
            ],
        ),
    ]
