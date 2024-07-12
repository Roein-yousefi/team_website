from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class TeamNews(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/' , blank=True , null=True)
    datetime_created = models.DateTimeField(auto_now_add=True , null=True , blank=True)

    def __str__(self):
        return self.title