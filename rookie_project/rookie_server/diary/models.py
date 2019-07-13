from django.db import models

class Diary(models.Model):
    date_time = models.DateTimeField(verbose_name='Shooting Date')
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

class Image(models.Model):
    image = models.ImageField(default='media/default_image.jpeg')