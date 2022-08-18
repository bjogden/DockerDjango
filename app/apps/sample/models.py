from django.db import models
from django.utils import timezone


class Sample(models.Model):
    name = models.TextField()

    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)
