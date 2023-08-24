from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser


class File(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField()

    def __str__(self):
        return self.name


class Consultant(models.Model):
    address = models.TextField()
    files = models.ManyToManyField(File, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Estate(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    Consultants = models.ManyToManyField(Consultant)

    def __str__(self):
        return self.name









