from django.db import models


# Create your models here.

class API(models.Model):
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=10)
    
    def __str__(self):
        return self.firstName
