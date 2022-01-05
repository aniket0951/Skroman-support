from django.contrib import admin
from django.urls import path
from .views import TestFun


urlpatterns = [
    path('openskroman/', TestFun),
]