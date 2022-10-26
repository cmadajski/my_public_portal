from django.db import models
from uuid import uuid4
from datetime import date

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=50, null=False)
    description = models.TextField(default='')
    github_url = models.CharField(max_length=128)
    deployed_url = models.CharField(max_length=128)
    img_url = models.CharField(max_length=128, default='#')

    def __str__(self):
        return self.title
        
    def fields(self):
        print('FIELDS: id | title | description | github_url | deployed_url')

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=128, null=False)
    description = models.TextField(default='N/A')
    url = models.CharField(max_length=64)
    content = models.TextField(default='N/A')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def generate_post_url(self):
        return '/get_blog_post/' + self.id + '/'

    def fields(self):
        print('FIELDS: id | title | description | url | content')

    class Meta:
        ordering = ['-date_posted']