from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
import json
from toys.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import *
# Create your views here.


def test_api_view(request):
    first_toys = Toys.objects.first()
    f_b = {
        'name': first_toys.name,
        'price': first_toys.price,
        'category': first_toys.category.from_category,
        'gender': first_toys.gender.gender,
        'toys_type': first_toys.toys_type.type,
        'delivery': first_toys.delivery.delivery,
    }
    return JsonResponse(f_b)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def toys_api_view(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return Response(data=ToysSerializer(instance=Toys.objects.all(), many=True).data, status=200)
        else:
            the_toys = get_object_or_404(Toys, pk=pk)
            return Response(data=ToysSerializer(instance=the_toys).data, status=200)

    elif request.method == "POST":
        sb = ToysSerializer(data=request.data)
        if sb.is_valid():
            sb.save()
            return Response({'id': sb.instance.id}, status=201)
        else:
            return Response(sb.error_messages, status=406)
    elif request.method == 'PUT':
        the_toys = get_object_or_404(Toys, pk=pk)
        sb = ToysSerializer(data=request.data, instance=the_toys)
        if sb.is_valid():
            sb.save()
            return Response('Updated', status=200)
        else:
            return Response(sb.error_messages, status=406)
    else:
        the_toys = get_object_or_404(Toys, pk=pk)
        the_toys.delete()
        return Response('Deleted', status=200)


class ToysListAPIView(ListAPIView):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer


class ToysCreateAPIView(CreateAPIView):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer


class ToysUpdateAPIView(UpdateAPIView):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer


class ToysDestroyAPIView(DestroyAPIView):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CountryiListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CategorySerializer


class CountryCreateAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdateAPIView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDestroyAPIView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionCreateAPIView(CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionUpdateAPIView(UpdateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDestroyAPIView(DestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CompanyListAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyUpdateAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDestroyAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class BrendListAPIView(ListAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class BrendCreateAPIView(CreateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class BrendUpdateAPIView(UpdateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class BrendDestroyAPIView(DestroyAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer


class GenderListAPIView(ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderCreateAPIView(CreateAPIView):
    queryset = Gender.objects.all()
    serializer_class = ToysSerializer


class GenderUpdateAPIView(UpdateAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class GenderDestroyAPIView(DestroyAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class Category_typeListAPIView(ListAPIView):
    queryset = Category_type.objects.all()
    serializer_class = Category_typeSerializer


class Category_typeCreateAPIView(CreateAPIView):
    queryset = Category_type.objects.all()
    serializer_class = Category_typeSerializer


class Category_typeUpdateAPIView(UpdateAPIView):
    queryset = Category_type.objects.all()
    serializer_class = Category_typeSerializer


class Category_typeDestroyAPIView(DestroyAPIView):
    queryset = Category_type.objects.all()
    serializer_class = Category_typeSerializer


class DeliveryListAPIView(ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryCreateAPIView(CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryUpdateAPIView(UpdateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DeliveryDestroyAPIView(DestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class OrderItemListAPIView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemCreateAPIView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemUpdateAPIView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDestroyAPIView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CouponListAPIView(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponCreateAPIView(CreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponUpdateAPIView(UpdateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponDestroyAPIView(DestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class Aksiya_CodeListAPIView(ListAPIView):
    queryset = Aksiya_Code.objects.all()
    serializer_class = Aksiya_CodeSerializer


class Aksiya_CodeCreateAPIView(CreateAPIView):
    queryset = Aksiya_Code.objects.all()
    serializer_class = Aksiya_CodeSerializer


class Aksiya_CodeUpdateAPIView(UpdateAPIView):
    queryset = Aksiya_Code.objects.all()
    serializer_class = Aksiya_CodeSerializer


class Aksiya_CodeDestroyAPIView(DestroyAPIView):
    queryset = Aksiya_Code.objects.all()
    serializer_class = Aksiya_CodeSerializer


class AksiyaListAPIView(ListAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer


class AksiyaCreateAPIView(CreateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer


class AksiyaUpdateAPIView(UpdateAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer


class AksiyaDestroyAPIView(DestroyAPIView):
    queryset = Aksiya.objects.all()
    serializer_class = AksiyaSerializer
