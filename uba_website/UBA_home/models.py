from django.db import models
from django.urls import reverse


# Other imported modules

from django.utils import timezone
import datetime

# Create your models here.

class member(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField()
    role = models.CharField(max_length=50)
    intro = models.TextField(default='', blank=True)
    

    def __str__(self):
        return f"{self.name}  |  {self.role} | "


class event(models.Model):
    PAST = 'done'
    CANCELLED = 'cancelled'
    FUTURE = 'yet_to_come'

    STATE_CHOICES = [
        (PAST, 'done'),
        (CANCELLED, 'cancelled'),
        (FUTURE, 'yet_to_come')
    ]



    state = models.CharField(max_length=20, choices=STATE_CHOICES, default = FUTURE)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    time_to_go = models.DurationField(null = True, blank = True)

    def save(self, *args, **kwargs):
        if self.state == self.FUTURE and self.date:
            current_time = timezone.now()
            time_difference = self.date - current_time
            self.time_to_go = time_difference

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']


