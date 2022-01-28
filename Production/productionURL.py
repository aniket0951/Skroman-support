from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('productionHome/', ProductionHomeClass.as_view(), name='production_home'),
]