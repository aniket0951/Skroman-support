from django.contrib import admin
from django.urls import path
from .views import addNewClient,editClientDetails, deleteLead,\
                   addLeadNote, SalesHomeClass, proccedLead

urlpatterns = [
    path('TestFuns/',SalesHomeClass.as_view(), name="testFuns"),
    path('addNewClient/<str:tag>/', addNewClient, name="addNewClient"),
    path('editClientDetails/<str:tag>/<str:lead_id>/', editClientDetails, name="editClientDetails"),
    path('deleteLead/<str:lead_id>/<str:tag>/', deleteLead, name="deleteLead"),
    path('addLeadNote/<str:lead_id>/', addLeadNote, name="addLeadNote"),

    # send lead to invantory after lead is active
    path('proccedLead/<str:lead_id>/', proccedLead, name="proccedLead" ),
]