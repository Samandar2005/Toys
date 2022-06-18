from django.shortcuts import render
from cmath import phase
from unicodedata import name
from urllib import response
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

# Create your views here.
