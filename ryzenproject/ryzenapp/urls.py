from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.homepage,name='Home'),
    path('Datas/', views.Datalist.as_view()),


]