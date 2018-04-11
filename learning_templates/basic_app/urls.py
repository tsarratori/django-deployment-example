from django.contrib import admin
from django.urls import path
from . import views


# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
path('other/',views.other,name="other"),
path('relative/',views.relative,name="relative")
]
