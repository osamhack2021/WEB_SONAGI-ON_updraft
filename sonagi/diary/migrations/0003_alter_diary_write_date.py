# Generated by Django 3.2.7 on 2021-10-17 04:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20211015_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='write_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='작성 일자'),
        ),
    ]
