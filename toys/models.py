from email.headerregistry import Address
from django.db import models

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
        return f"{self.username}"


class Category(models.Model):
    from_category = models.IntegerField()
    to_category = models.IntegerField()

    def __str__(self):
        return f"{self.from_category} {self.to_category}"


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.country}"


class Brend(models.Model):
    name = models.CharField(max_length=50)
    companiy_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.companiy_id}"


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

    def __str__(self):
        return f"{self.name} {self.price} {self.category} {self.gender} {self.toys_type} {self.img} {self.delivery}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    toys = models.ForeignKey(Toys, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.user} {self.toys}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    toys = models.ForeignKey(
        Toys, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.SmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.order} {self.toys} {self.price} {self.quantity}"


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.code} {self.valid_from} {self.valid_to} {self.status}"


class Aksiya_Code(models.Model):
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.date_from} {self.date_to}"


class Aksiya(models.Model):
    name = models.CharField(max_length=50)
    old_price = models.FloatField()
    new_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    toys_type = models.ForeignKey(Category_type, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/images')
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    chegirma = models.ImageField()
    code = models.ForeignKey(Aksiya_Code, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.old_price} {self.new_price} {self.chegirma} {self.category} {self.gender} {self.toys_type} {self.img} {self.delivery} {self.chegirma} {self.code}"
