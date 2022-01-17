from django.contrib import admin
from django.urls import path
from .views import TestFun, addNewClient,editClientDetails, deleteLead,\
                   addLeadNote

urlpatterns = [
    path('TestFuns/', TestFun, name="testFuns"),
    path('addNewClient/<str:tag>/', addNewClient, name="addNewClient"),
    path('editClientDetails/<str:tag>/<str:lead_id>/', editClientDetails, name="editClientDetails"),
    path('deleteLead/<str:lead_id>/<str:tag>/', deleteLead, name="deleteLead"),
    path('addLeadNote/<str:lead_id>/', addLeadNote, name="addLeadNote"),
]