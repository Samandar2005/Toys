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
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request, "about.html")
# Create your views here.

@login_required
def profile(request):
    return render(request, 'user-profile.html')


def order(request):
    return render(request, 'order.html')


def index(request):
    bks = Toys.objects.all()
    context = {'toys': bks}
    return render(request, "base.html", context=context)


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
    template_name = 'category-add.html'
    fields = "__all__"

    success_url = '/category'


class CategoryUpdateView(UpdateView):
    queryset = Category.objects.all()
    template_name = 'category-add.html'
    fields = "__all__"
    success_url = '/category'


class CategoryDeleteView(DeleteView):
    queryset = Category.objects.all()
    template_name = 'category-delete.html'
    fields = "__all__"

    success_url = '/category'


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
    template_name = 'gender-add.html'
    fields = "__all__"

    success_url = '/gender'


class GenderUpdateView(UpdateView):
    queryset = Gender.objects.all()
    template_name = 'gender-add.html'
    fields = "__all__"
    success_url = '/gender'


class GenderDeleteView(DeleteView):
    queryset = Gender.objects.all()
    template_name = 'gender-delete.html'
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
    template_name = 'category_type-add.html'
    fields = "__all__"

    success_url = '/category_type'


class Category_typeUpdateView(UpdateView):
    queryset = Category_type.objects.all()
    template_name = 'category_type-add.html'
    fields = "__all__"
    success_url = '/category_type'


class Category_typeDeleteView(DeleteView):
    queryset = Category_type.objects.all()
    template_name = 'category_type-delete.html'
    fields = "__all__"

    success_url = '/category_type'


class ImgListView(ListView):
    template_name = 'img.html'
    context_object_name = 'img'

    def get_queryset(self):
        url_data = self.request.GET
        q = Img.objects.all()
        return q


class ImgCreateView(CreateView):
    queryset = Img.objects.all()
    template_name = 'img-add.html'
    fields = "__all__"

    success_url = '/img'


class ImgUpdateView(UpdateView):
    queryset = Img.objects.all()
    template_name = 'img-add.html'
    fields = "__all__"
    success_url = '/img'


class ImgDeleteView(DeleteView):
    queryset = Img.objects.all()
    template_name = 'img-delete.html'
    fields = "__all__"

    success_url = '/img'

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
    queryset = Category_type.objects.all()
    template_name = 'delivery-add.html'
    fields = "__all__"

    success_url = '/delivery'


class DeliveryUpdateView(UpdateView):
    queryset = Category_type.objects.all()
    template_name = 'delivery-add.html'
    fields = "__all__"
    success_url = '/delivery'


class DeliveryDeleteView(DeleteView):
    queryset = Category_type.objects.all()
    template_name = 'delivery-delete.html'
    fields = "__all__"

    success_url = '/delivery'


class ToysListView(ListView):
    template_name = 'shoes-1.html'
    context_object_name = 'shoes'

    def get_queryset(self):
        xaridor = Group.objects.get(name='Xaridor')
        if self.request.user.has_perm("can_view_toys") or xaridor in self.request.user.groups.all():
            q = Toys.objects.all()
            return q


class ToysCreateView(CreateView):
    queryset = Toys.objects.all()
    template_name = 'toys-add.html'
    fields = "__all__"

    success_url = '/toys'


class ToysUpdateView(UpdateView):
    queryset = Toys.objects.all()
    template_name = 'toys-add.html'
    fields = "__all__"

    success_url = '/toys'


class ToysDeleteView(DeleteView):
    queryset = Toys.objects.all()
    template_name = 'toys-delete.html'
    fields = "__all__"

    success_url = '/toys'



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
                return redirect('shoes')
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

            return redirect('shoes')
        else:
            return render(request, template_name='user-register.html', context={'form': form})


# class ShoesListViewMain(ListView):
#     queryset = Shoes.objects.all()
#     template_name = 'shoes_base.html'
#     context_object_name = 'shoes'
