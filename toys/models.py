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
        return f"{self.username}"


class Category(models.Model):
    from_category = models.IntegerField()
    to_category = models.IntegerField()

    def __str__(self):
        return f"{self.from_category} {self.to_category}"


class Gender(models.Model):
    gender = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gender}"


class Category_type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.type}"


class Delivery(models.Model):
    delivery = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.delivery}"


class Toys(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    toys_type = models.ForeignKey(Category_type, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/images')
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.price} {self.category} {self.gender} {self.toys_type} {self.img} {self.delivery}"

    def save(self) -> None:
        return super().save()
