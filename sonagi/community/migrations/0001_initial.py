# Generated by Django 3.2.7 on 2021-10-17 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import sonagi.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='게시판 이름')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('content', models.CharField(max_length=2000, null=True, verbose_name='내용')),
                ('image', models.ImageField(blank=True, upload_to=sonagi.utils.RandomFileName('postimage'), verbose_name='게시글 이미지')),
                ('is_notice', models.BooleanField(default=False, verbose_name='공지사항 여부')),
                ('write_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성 일자')),
                ('rewrite_date', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일자')),
                ('board_id', models.ForeignKey(db_column='board_id', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='community.board')),
                ('email', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, null=True, verbose_name='내용')),
                ('write_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성 일자')),
                ('rewrite_date', models.DateTimeField(auto_now=True, verbose_name='최종 수정 일자')),
                ('email', models.ForeignKey(db_column='email', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL, to_field='email')),
                ('post_id', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='community.post')),
            ],
        ),
    ]
