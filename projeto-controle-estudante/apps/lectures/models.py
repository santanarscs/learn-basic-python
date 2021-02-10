from django.db import models

from apps.utils.models import Timestamps


class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='', blank=True)
    date = models.DateTimeField()
    duration = models.IntegerField(help_text='Enter number of hours')
    slides_url = models.CharField(max_length=255)
    is_required = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
