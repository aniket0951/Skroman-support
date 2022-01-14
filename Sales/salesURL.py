from django.contrib import admin
from django.urls import path
from .views import TestFun, addNewClient,editClientDetails, deleteLead

urlpatterns = [
    path('TestFuns/', TestFun, name="testFuns"),
    path('addNewClient/<str:tag>/', addNewClient, name="addNewClient"),
    path('editClientDetails/', editClientDetails, name="editClientDetails"),
    path('deleteLead/<str:lead_id>/', deleteLead, name="deleteLead"),
]