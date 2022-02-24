# Generated by Django 3.2.10 on 2022-02-17 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220216_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]