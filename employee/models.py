from django.db import models

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=200)
    titles = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
