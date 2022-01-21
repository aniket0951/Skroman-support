from django.contrib import admin
from django.urls import path
from .views import InvantoryHomeClass, BOMListClass, AddBOM

urlpatterns = [
    path('invantoryHome/', InvantoryHomeClass.as_view(), name="openInvantory"),
    path('bomList/', BOMListClass.as_view(), name='BOMListClass'),
    path('AddBOM/', AddBOM, name="AddBOM"),
]