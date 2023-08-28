from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('', filename)




class File(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                        verbose_name=('media/images/'))
    description = models.TextField()

    def __str__(self):
        return self.name


class Consultant(models.Model):
    address = models.TextField()
    files = models.ManyToManyField(File, blank=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.get_username()


class Estate(models.Model):
    EstateName = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.TextField()
    Consultants = models.ManyToManyField(Consultant)

    def __str__(self):
        return self.EstateName


