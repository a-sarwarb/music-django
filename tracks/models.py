from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
User = settings.AUTH_USER_MODEL
# Create your models here.
class Song(models.Model):
    songs = models.FileField(upload_to='media/')
    category = models.CharField(max_length=25)
    name = models.CharField(max_length=30, blank=False)
    singer = models.CharField(max_length=20, blank=False)
    likes = models.ManyToManyField(User, related_name='like_music')
    dislikes = models.ManyToManyField(User, related_name='dislike_music')

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse('song_detail', args=[str(self.id)])