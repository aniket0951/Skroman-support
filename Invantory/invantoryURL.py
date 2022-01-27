from django.contrib import admin
from django.urls import path
from .views import InvantoryHomeClass, BOMListClass, AddBOM,\
                   BOMVerification

urlpatterns = [
    path('invantoryHome/', InvantoryHomeClass.as_view(), name="openInvantory"),
    path('bomList/', BOMListClass.as_view(), name='BOMListClass'),
    path('AddBOM/', AddBOM, name="addBOM"),
    path('BOMVerification/<str:tag>/<str:lead_id>/', BOMVerification, name='bom_verification'),
]