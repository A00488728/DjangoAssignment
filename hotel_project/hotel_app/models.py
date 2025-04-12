from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    stars = models.IntegerField(default=3)  # Optional

    def __str__(self):
        return self.name
