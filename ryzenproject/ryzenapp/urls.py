from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.homepage,name='Home'),
    path('Datas/<int:x>', views.name_detail),


]