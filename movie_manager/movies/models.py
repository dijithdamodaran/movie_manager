from django.db import models

# Create your models here.
class movieinfo(models.Model):
    title=models.CharField(max_length=50)
    year=models.IntegerField(null=True)
    description=models.TextField()

class Director(models.Model):
    name=models.CharField(max_length=50)
