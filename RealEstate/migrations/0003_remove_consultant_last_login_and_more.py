# Generated by Django 4.2.4 on 2023-08-24 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate', '0002_alter_consultant_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultant',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='password',
        ),
    ]