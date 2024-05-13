# Generated by Django 4.2.11 on 2024-05-02 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0004_alter_userdetails_remaining_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='remaining_time',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='expirt_Date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
