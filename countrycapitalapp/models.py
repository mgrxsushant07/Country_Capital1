from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=150)
    capital = models.CharField(max_length=150)
    population = models.IntegerField()
    official_language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    def __str__(self):
        return self.name
