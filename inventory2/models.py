from django.db import models

# Create your models here.

class inventory(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    tool = models.CharField(max_length=200)
    specs = models.CharField(max_length=200)
    


