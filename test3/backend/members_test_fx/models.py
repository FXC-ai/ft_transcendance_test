from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.fields.CharField(max_length=100)

class Games(models.Model):
    title = models.fields.CharField(max_length=100)