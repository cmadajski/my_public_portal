# Generated by Django 4.1.2 on 2022-10-23 23:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(default='N/A', max_length=128)),
                ('description', models.TextField(default='N/A')),
                ('url', models.CharField(max_length=64)),
            ],
        ),
    ]
