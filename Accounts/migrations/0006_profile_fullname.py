# Generated by Django 4.2.11 on 2024-04-04 03:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]