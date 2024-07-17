from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class TeamNews(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='newas/' , blank=True , null=True)
    datetime_created = models.DateTimeField(auto_now_add=True , null=True , blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.id])

class TeamShop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='newas/' , blank=True , null=True)
    datetime_created = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    price = models.IntegerField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop-detail' , args=[self.id])

class ShopComment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    shop = models.ForeignKey(TeamShop , on_delete=models.CASCADE , related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)


class TeamGallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='newas/' , blank=True , null=True)
    datetime_created = models.DateTimeField(auto_now_add=True , null=True , blank=True)

    def __str__(self):
        return self.title


class TeamPlayer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='newas/' , blank=True , null=True)
    description = models.TextField()

    def __str__(self):
        return self.name