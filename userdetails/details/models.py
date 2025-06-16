from django.db import models

# Create your models here.
from django.db import models

class UserInformation(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.name
