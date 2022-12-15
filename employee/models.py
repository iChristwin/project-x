from django.db import models

# Create your models here.


class Register(models.Model):
    f1name = models.CharField("Name", max_length=200)
    email = models.CharField("Email",max_length=200)
    phone = models.CharField("Phone",max_length=200)
    why = models.CharField("Why does the student need tutoring", max_length=2000)


class Tutor(models.Model):
    f1name = models.CharField("Name", max_length=200)
    email = models.CharField("Email",max_length=200)
    phone = models.CharField("Phone",max_length=200)
    you = models.CharField("Tell us about yourself",max_length=2000)

class Subscribe(models.Model):
    Email = models.CharField("Email", max_length=200)


