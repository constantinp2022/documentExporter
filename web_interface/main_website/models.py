from django.db import models

from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_publish = models.DateField(default=timezone.now)
    time_publish = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.title
