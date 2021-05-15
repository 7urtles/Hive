from django.db import models
from django.urls import reverse

# Create your models here.

class Counting(models.Model):
    company = models.CharField(max_length=200)
    entered = models.IntegerField(default=0)
    exited = models.IntegerField(default=0)
    current_total = models.IntegerField(default=0)
    building_capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('home', args=[str(self.pk)])