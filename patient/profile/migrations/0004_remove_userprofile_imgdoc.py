# Generated by Django 3.2 on 2021-04-08 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0003_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='imgDoc',
        ),
    ]
