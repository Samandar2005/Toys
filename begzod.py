from collections import UserString
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import *


# Create your models here.
class User(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    img = models.ImageField()

    class Meta:
        ordering = ["-username"]

    def __str__(self):
        return self.username


class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"


class Company(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.title}"


class condition(models.Model):
    condition = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.condition}"


class size(models.Model):
    size = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.size}"


class technique(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.FloatField()
    abaut = models.CharField(max_length=500)
    img = models.ImageField(upload_to='static/images')
    condition = models.ForeignKey(condition, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    size = models.ForeignKey(size, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.company} {self.price} {self.brand} {self.img}  {self.color} "

    def save(self):
        return super().save()
