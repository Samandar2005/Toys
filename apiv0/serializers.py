from rest_framework import serializers
from toys.models import *


class ToysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Toys
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class BrendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brend
        fields = '__all__'


class GenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gender
        fields = '__all__'


class Category_typeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category_type
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = '__all__'


class Aksiya_CodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aksiya_Code
        fields = '__all__'


class AksiyaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aksiya
        fields = '__all__'
