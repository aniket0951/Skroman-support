from django.contrib import admin
from django.urls import path
from .views import InvantoryHomeClass

urlpatterns = [
    path('invantoryHome/', InvantoryHomeClass.as_view(), name="openInvantory")
]