from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Members(models.Model):

    def __str__(self):
        return f'{self.name}'

    class connection(models.TextChoices):
        HORS_LIGNE = "hors ligne"
        ONLINE = "online"
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(default="default")
    age = models.fields.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(150)])
    active = models.fields.BooleanField(default=True)
    connection_state = models.fields.CharField(max_length=10, choices=connection.choices, default=connection.HORS_LIGNE)

class Games(models.Model):
    title = models.fields.CharField(max_length=100)
    members = models.ForeignKey(Members, null=True, on_delete=models.SET_NULL)