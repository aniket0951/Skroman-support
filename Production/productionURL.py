from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('productionHome/', ProductionHomeClass.as_view(), name='production_home'),

    # to assign the work for a team by production head
    path('WorkOnDevice/<str:lead_id>/<str:device_id>/', WorkOnDevice, name='work_on_device'),

    # to verify the bom list of selected device
    path('BomVerification/<str:device_id>/', BomVerification, name='bom_verification'), 

    # show all prodution user detial
    path('ProductionUser/<str:tag>/', ProductionUsers, name='production_user'),

    # show daily task to all production members
    path('DailyTasks/<str:auth_token>/', DailyTasks, name='daily_tasks'),
]