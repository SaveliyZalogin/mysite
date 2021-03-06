"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from .apps.mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.none_url, name='none_url'),
    path('login/', views.user_login, name='login'),
    path('main/', views.index, name='mainpage'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    re_path(r'^news/(?P<news_id>\d+)$', views.news, name="news"),
]
