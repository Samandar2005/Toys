from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
