from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    participants = models.ManyToManyField(User, related_name='events', blank=True)
    
    def __str__(self):
        return self.title
