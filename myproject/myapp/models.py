from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    event= models.CharField(max_length=19)
    date = models.DateField()
