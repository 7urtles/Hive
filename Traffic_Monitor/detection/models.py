from django.db import models
from django.urls import reverse

# Create your models here.

class Company(models.Model):
    company = models.CharField(max_length=200)
    entered = models.IntegerField(default=0)
    exited = models.IntegerField(default=0)
    current = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return reverse('counts_detail', args=[str(self.pk)])

class Entrance(models.Model):

    timeIn = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('movement_detail', args=[str(self.pk)])

class Exit(models.Model):

    timeOut = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('movement_detail', args=[str(self.pk)])