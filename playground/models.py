from django.db import models

# Create your models here.

class Book(models.Model):
    gid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    cname=models.CharField(max_length=200)

