from django.contrib import admin
from django.urls import path
from .views import TestFun, LoginUser, VerifyOtp


urlpatterns = [
    path('openskroman/', TestFun),
    path('loginUser/', LoginUser, name="loginUser"),
    path('VerifyOtp/', VerifyOtp, name="verifyOtp"),
]