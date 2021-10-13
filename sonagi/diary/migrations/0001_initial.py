# Generated by Django 2.2.4 on 2021-10-12 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='한줄평')),
                ('content', models.CharField(max_length=2000, null=True, verbose_name='내용')),
                ('emotion', models.CharField(choices=[('G', '좋음'), ('N', '보통'), ('B', '별로'), ('C', '슬픔'), ('S', '놀람')], max_length=1, verbose_name='감정')),
                ('write_date', models.DateField(auto_now_add=True, verbose_name='작성 일자')),
                ('rewrite_date', models.DateField(auto_now=True, verbose_name='최종 수정 일자')),
                ('email', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, related_name='diary', to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
        ),
    ]