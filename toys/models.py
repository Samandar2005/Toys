from django.db import models

# Create your models here.

class Users(models.Model):
  last_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  email = models.EmailField()
  img = models.ImageField()

  class Meta:
    ordering = ["-username"]

  def __str__(self):
    return self.username

class Category(models.Model):
  from_category = models.FloatField()
  to_category = models.FloatField()

  def __str__(self):
    return self.from_category, self.to_category


class Gender(models.Model):
  gender = models.CharField(max_length=50)

  def __str__(self):
    return self.gender

class Category_type(models.Model):
  type = models.CharField(max_length=50)

  def __str__(self):
    return self.type

class Img(models.Model):
  img = models.ImageField()


class Delivery(models.Model):
  delivery = models.CharField(max_length=50)

  def __str__(self):
    return self.delivery

class Toys(models.Model):
  name = models.CharField(max_length=50)
  price = models.FloatField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
  type = models.ForeignKey(Category_type, on_delete=models.CASCADE)
  img = models.ForeignKey(Img, on_delete=models.CASCADE)
  delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
