# Generated by Django 4.1.2 on 2022-10-23 22:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(default='N/A', max_length=50)),
                ('description', models.TextField(default='')),
                ('github_url', models.CharField(max_length=128)),
                ('deployed_url', models.CharField(max_length=128)),
            ],
        ),
    ]
