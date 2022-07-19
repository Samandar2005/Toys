from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['from_category', 'to_category']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'region']


@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    list_display = ['name', 'companiy_id']


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['gender']


@admin.register(Category_type)
class Category_typeAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['delivery']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'toys', 'price', 'quantity']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'status']


@admin.register(Aksiya_Code)
class Aksiya_CodeAdmin(admin.ModelAdmin):
    list_display = ['date_from', 'date_to']


@admin.register(Aksiya)
class AksiyaAdmin(admin.ModelAdmin):
    list_display = ['name', 'old_price', 'new_price', 'category',
                    'brend', 'gender', 'toys_type', 'img', 'delivery', 'code']


@admin.register(Toys)
class ToysAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'price', 'category', 'brend', 'gender', 'toys_type', 'delivery']
    list_filter = ["category", 'price']
    search_fields = ["name__icontains"]

    def show_buy(self, obj):
        return format_html(f"<a href='sssss'>buy</a>")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'toys']

    fields = ['toys']
