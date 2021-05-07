from django.db import models
from django.urls import reverse

# Create your models here.


class Music(models.Model):
    name = models.TextField()
    artist = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music_info')
