# Generated by Django 4.2.11 on 2024-04-05 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_profile_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/avatar7.png', upload_to='images/'),
        ),
    ]