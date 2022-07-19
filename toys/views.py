from cmath import phase
from unicodedata import name
from urllib import response
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request, "about.html")


@login_required
def profile(request):
    return render(request, 'user-profile.html')


def order(request):
    return render(request, 'order.html')

def abs(request):
    return render(request, 'abs.html')

def contact(request):
    return render(request, 'contact.html')


def main_register(request):
    return render(request, 'main-register.html')


def clients(request):
    return render(request, 'clients.html')


def testmonial(request):
    return render(request, 'testmonial.html')


def index(request):
    bks = Toys.objects.all()
    bks1 = Aksiya.objects.all()
    context = {'toys': bks, 'aksiya': bks1}
    return render(request, "index.html", context=context)


class CategoryListView(ListView):
    template_name = 'category.html'
    context_object_name = 'category'

    def get_queryset(self):
        url_data = self.request.GET
        q = Category.objects.all()
        if 'from_category' in url_data and url_data['from_category']:
            q = q.filter(from_category__icontains=url_data['from_category'])
        return q


class CategoryCreateView(CreateView):
    queryset = Category.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/category'


class CategoryUpdateView(UpdateView):
    queryset = Category.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/category'


class CategoryDeleteView(DeleteView):
    queryset = Category.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/category'


class RegionListView(ListView):
    template_name = 'region.html'
    context_object_name = 'region'

    def get_queryset(self):
        url_data = self.request.GET
        q = Region.objects.all()
        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class RegionCreateView(CreateView):
    queryset = Region.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/region'


class RegionUpdateView(UpdateView):
    queryset = Region.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/region'


class RegionDeleteView(DeleteView):
    queryset = Region.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/region'


class CountryListView(ListView):
    template_name = 'country.html'
    context_object_name = 'country'

    def get_queryset(self):
        url_data = self.request.GET
        q = Country.objects.all()
        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class CountryCreateView(CreateView):
    queryset = Country.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/country'


class CountryUpdateView(UpdateView):
    queryset = Country.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/country'


class CountryDeleteView(DeleteView):
    queryset = Country.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/country'


class CompanyListView(ListView):
    template_name = 'company.html'
    context_object_name = 'company'

    def get_queryset(self):
        url_data = self.request.GET
        q = Company.objects.all()
        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class CompanyCreateView(CreateView):
    queryset = Company.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/company'


class CompanyUpdateView(UpdateView):
    queryset = Company.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/company'


class CompanyDeleteView(DeleteView):
    queryset = Company.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/company'


class BrendListView(ListView):
    template_name = 'brend.html'
    context_object_name = 'brend'

    def get_queryset(self):
        url_data = self.request.GET
        q = Brend.objects.all()
        if 'name' in url_data and url_data['name']:
            q = q.filter(name__icontains=url_data['name'])
        return q


class BrendCreateView(CreateView):
    queryset = Brend.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/brend'


class BrendUpdateView(UpdateView):
    queryset = Brend.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/brend'


class BrendDeleteView(DeleteView):
    queryset = Brend.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/brend'


class GenderListView(ListView):
    template_name = 'gender.html'
    context_object_name = 'gender'

    def get_queryset(self):
        url_data = self.request.GET
        q = Gender.objects.all()

        if 'gender' in url_data and url_data['gender']:
            q = q.filter(gender__icontains=url_data['gender'])
        return q


class GenderCreateView(CreateView):
    queryset = Gender.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/gender'


class GenderUpdateView(UpdateView):
    queryset = Gender.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/gender'


class GenderDeleteView(DeleteView):
    queryset = Gender.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/gender'


class Category_typeListView(ListView):
    template_name = 'category_type.html'
    context_object_name = 'category_type'

    def get_queryset(self):
        url_data = self.request.GET
        q = Category_type.objects.all()

        if 'type' in url_data and url_data['type']:
            q = q.filter(type__icontains=url_data['type'])
        return q


class Category_typeCreateView(CreateView):
    queryset = Category_type.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/category_type'


class Category_typeUpdateView(UpdateView):
    queryset = Category_type.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/category_type'


class Category_typeDeleteView(DeleteView):
    queryset = Category_type.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/category_type'


class DeliveryListView(ListView):
    template_name = 'delivery.html'
    context_object_name = 'delivery'

    def get_queryset(self):
        url_data = self.request.GET
        q = Delivery.objects.all()

        if 'delivery' in url_data and url_data['delivery']:
            q = q.filter(delivery__icontains=url_data['delivery'])
        return q


class DeliveryCreateView(CreateView):
    queryset = Delivery.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/delivery'


class DeliveryUpdateView(UpdateView):
    queryset = Delivery.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/delivery'


class DeliveryDeleteView(DeleteView):
    queryset = Delivery.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/delivery'


class ToysListView(ListView):
    template_name = 'toys.html'
    context_object_name = 'toys'

    def get_queryset(self):
        url_data = self.request.GET
        q = Toys.objects.all()
        return q


class ToysCreateView(CreateView):
    queryset = Toys.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/toys'


class ToysUpdateView(UpdateView):
    queryset = Toys.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/toys'


class ToysDeleteView(DeleteView):
    queryset = Toys.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/toys'


class CouponListView(ListView):
    template_name = 'coupon.html'
    context_object_name = 'coupon'

    def get_queryset(self):
        url_data = self.request.GET
        q = Coupon.objects.all()

        if 'code' in url_data and url_data['code']:
            q = q.filter(code__icontains=url_data['code'])
        return q


class CouponCreateView(CreateView):
    queryset = Coupon.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/coupon'


class CouponUpdateView(UpdateView):
    queryset = Coupon.objects.all()
    template_name = 'add.html'
    fields = "__all__"
    success_url = '/coupon'


class CouponDeleteView(DeleteView):
    queryset = Coupon.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/coupon'


class AksiyaListView(ListView):
    template_name = 'aksiya.html'
    context_object_name = 'aksiya'

    def get_queryset(self):
        url_data = self.request.GET
        q = Aksiya.objects.all()
        return q


class AksiyaCreateView(CreateView):
    queryset = Aksiya.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/aksiya'


class AksiyaUpdateView(UpdateView):
    queryset = Aksiya.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/aksiya'


class AksiyaDeleteView(DeleteView):
    queryset = Aksiya.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/aksiya'


class Aksiya_CodeListView(ListView):
    template_name = 'aksiya_code.html'
    context_object_name = 'aksiya_code'

    def get_queryset(self):
        url_data = self.request.GET
        q = Aksiya_Code.objects.all()
        return q


class Aksiya_CodeCreateView(CreateView):
    queryset = Aksiya_Code.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/aksiya_code'


class Aksiya_CodeUpdateView(UpdateView):
    queryset = Aksiya_Code.objects.all()
    template_name = 'add.html'
    fields = "__all__"

    success_url = '/aksiya_code'


class Aksiya_CodeDeleteView(DeleteView):
    queryset = Aksiya_Code.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/aksiya_code'


def user_login_view(request):
    if request.method == 'GET':
        form = UserLoginForm()
        return render(request, template_name='user-login.html', context={'form': form})
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect('main')
            else:
                return render(request, template_name='user-login.html', context={'form': form})


def user_register_view(request):
    if request.method == 'GET':
        form = UserRegisterModelForm()

        return render(request, template_name='user-register.html', context={'form': form})
    else:
        form = UserRegisterModelForm(data=request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and password == confirm:
            form.save()
            user = form.instance
            user.groups.add(Group.objects.get(name='Xaridor'))
            user.save()

            login(request, user)

            return redirect('main')
        else:
            return render(request, template_name='user-register.html', context={'form': form})
