from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', index),
    path('main/', index, name='main'),
    path('about/', about, name='about'),
    path('testmonial/', testmonial, name='testmonial'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/add', CategoryCreateView.as_view(), name='category-add'),
    path('category/change/<int:pk>', CategoryUpdateView.as_view(), name='category-change'),
    path('category/delete/<int:pk>', CategoryDeleteView.as_view(), name='category-delete'),
    path('gender/', GenderListView.as_view(), name='gender'),
    path('gender/add', GenderCreateView.as_view(), name='gender-add'),
    path('gender/change/<int:pk>',
         GenderUpdateView.as_view(), name='gender-change'),
    path('gender/delete/<int:pk>',
         GenderDeleteView.as_view(), name='gender-delete'),

    path('category_type/', Category_typeListView.as_view(), name='category_type'),
    path('category_type/add', Category_typeCreateView.as_view(), name='category_type-add'),
    path('category_type/change/<int:pk>',
         Category_typeUpdateView.as_view(), name='category_type-change'),
    path('category_type/delete/<int:pk>',
         Category_typeDeleteView.as_view(), name='category_type-delete'),

    path('delivery/', DeliveryListView.as_view(), name='delivery'),
    path('delivery/add', DeliveryCreateView.as_view(), name='delivery-add'),
    path('delivery/change/<int:pk>',
         DeliveryUpdateView.as_view(), name='delivery-change'),
    path('delivery/delete/<int:pk>',
         DeliveryDeleteView.as_view(), name='delivery-delete'),

    path('toys/', ToysListView.as_view(), name='toys'),
    path('toys/add', ToysCreateView.as_view(), name='toys-add'),
    path('toys/change/<int:pk>',
         ToysUpdateView.as_view(), name='toys-change'),
    path('toys/delete/<int:pk>',
         ToysDeleteView.as_view(), name='toys-delete'),
]
