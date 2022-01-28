from django.contrib import admin
from django.urls import path
from .views import InvantoryHomeClass, BOMListClass, AddBOM,\
                   BOMVerification, showComponentInfo, ProceedProduction

urlpatterns = [
    path('invantoryHome/', InvantoryHomeClass.as_view(), name="openInvantory"),
    path('bomList/', BOMListClass.as_view(), name='BOMListClass'),
    path('AddBOM/', AddBOM, name="addBOM"),

    # for bom verification
    path('BOMVerification/<str:tag>/<str:lead_id>/', BOMVerification, name='bom_verification'),
    
    # showing component info from device 
    path('showComponentInfo/<str:model_name>/<str:quantity>/<str:device_id>/', showComponentInfo, name='showComponentInfo'),

    # proceed to production the lead work
    path('ProceedProduction/<str:lead_id>/', ProceedProduction, name='proceed_production'),
]