# Generated by Django 4.2.11 on 2024-05-01 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Attendance', '0002_rename_expiry_time_attendancecode_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('shift', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('remaining_time', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
