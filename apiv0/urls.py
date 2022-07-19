from django.urls import include, path
from .views import *


urlpatterns = [
    path('test-api-view/', test_api_view),
    path('toys-api-view/', ToysListAPIView.as_view()),
    path('toys-api-view/create', ToysCreateAPIView.as_view()),
    path('toys-api-view/update/<int:pk>', ToysUpdateAPIView.as_view()),
    path('toys-api-view/delete/<int:pk>', ToysDestroyAPIView.as_view()),

    path('category-api-view/', CategoryListAPIView.as_view()),
    path('category-api-view/create', CategoryCreateAPIView.as_view()),
    path('category-api-view/update/<int:pk>', CategoryUpdateAPIView.as_view()),
    path('category-api-view/delete/<int:pk>',
         CategoryDestroyAPIView.as_view()),

    path('country-api-view/', CountryiListAPIView.as_view()),
    path('country-api-view/create', CountryCreateAPIView.as_view()),
    path('country-api-view/update/<int:pk>', CountryUpdateAPIView.as_view()),
    path('country-api-view/delete/<int:pk>', CountryDestroyAPIView.as_view()),

    path('region-api-view/', RegionListAPIView.as_view()),
    path('region-api-view/create', RegionCreateAPIView.as_view()),
    path('region-api-view/update/<int:pk>', RegionUpdateAPIView.as_view()),
    path('region-api-view/delete/<int:pk>', RegionDestroyAPIView.as_view()),

    path('company-api-view/', CompanyListAPIView.as_view()),
    path('company-api-view/create', CompanyCreateAPIView.as_view()),
    path('company-api-view/update/<int:pk>', CompanyUpdateAPIView.as_view()),
    path('company-api-view/delete/<int:pk>', CompanyDestroyAPIView.as_view()),

    path('brend-api-view/', BrendListAPIView.as_view()),
    path('brend-api-view/create', BrendCreateAPIView.as_view()),
    path('brend-api-view/update/<int:pk>', BrendUpdateAPIView.as_view()),
    path('brend-api-view/delete/<int:pk>', BrendDestroyAPIView.as_view()),

    path('gender-api-view/', GenderListAPIView.as_view()),
    path('gender-api-view/create', GenderCreateAPIView.as_view()),
    path('gender-api-view/update/<int:pk>', GenderUpdateAPIView.as_view()),
    path('gender-api-view/delete/<int:pk>', GenderDestroyAPIView.as_view()),

    path('category_type-api-view/', Category_typeListAPIView.as_view()),
    path('category_type-api-view/create', Category_typeCreateAPIView.as_view()),
    path('category_type-api-view/update/<int:pk>',
         Category_typeUpdateAPIView.as_view()),
    path('category_type-api-view/delete/<int:pk>',
         Category_typeDestroyAPIView.as_view()),

    path('delivery-api-view/', DeliveryListAPIView.as_view()),
    path('delivery-api-view/create', DeliveryCreateAPIView.as_view()),
    path('delivery-api-view/update/<int:pk>', DeliveryUpdateAPIView.as_view()),
    path('delivery-api-view/delete/<int:pk>',
         DeliveryDestroyAPIView.as_view()),

    path('orderitem-api-view/', OrderItemListAPIView.as_view()),
    path('orderitem-api-view/create', OrderItemCreateAPIView.as_view()),
    path('orderitem-api-view/update/<int:pk>',
         OrderItemUpdateAPIView.as_view()),
    path('orderitem-api-view/delete/<int:pk>',
         OrderItemDestroyAPIView.as_view()),

    path('coupon-api-view/', CouponListAPIView.as_view()),
    path('coupon-api-view/create', CouponCreateAPIView.as_view()),
    path('coupon-api-view/update/<int:pk>', CouponUpdateAPIView.as_view()),
    path('coupon-api-view/delete/<int:pk>', CouponDestroyAPIView.as_view()),

    path('aksiya_code-api-view/', Aksiya_CodeListAPIView.as_view()),
    path('aksiya_code-api-view/create', Aksiya_CodeCreateAPIView.as_view()),
    path('aksiya_code-api-view/update/<int:pk>',
         Aksiya_CodeUpdateAPIView.as_view()),
    path('aksiya_code-api-view/delete/<int:pk>',
         Aksiya_CodeDestroyAPIView.as_view()),

    path('toys-api-view/', AksiyaListAPIView.as_view()),
    path('toys-api-view/create', AksiyaCreateAPIView.as_view()),
    path('toys-api-view/update/<int:pk>', AksiyaUpdateAPIView.as_view()),
    path('toys-api-view/delete/<int:pk>', AksiyaDestroyAPIView.as_view()),

    path('toys-api-view/<int:pk>/', toys_api_view),


    path('auth/', include('rest_framework.urls')),
]
