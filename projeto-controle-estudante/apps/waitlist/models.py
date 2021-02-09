from django.db import models

from apps.utils.models import Timestamps


class WaitlistEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, verbose_name='email address', unique=True)
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Waitlist Entries'

    def __str__(self):
        return self.first_name
