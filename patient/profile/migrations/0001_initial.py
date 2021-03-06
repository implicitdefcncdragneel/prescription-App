# Generated by Django 3.2 on 2021-04-08 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('q1', models.CharField(default=False, max_length=200)),
                ('q2', models.CharField(default=False, max_length=200)),
                ('q3', models.CharField(default=False, max_length=200)),
                ('q4', models.CharField(default=False, max_length=200)),
                ('q5', models.CharField(default=False, max_length=200)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('imgDoc', models.ImageField(upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile_patient',
            },
        ),
    ]
