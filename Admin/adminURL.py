from django.contrib import admin
from django.urls import path
from .views import TestFun, LoginUser, AllUsers, AddNewUser

urlpatterns = [
    path('openskroman/', TestFun),
    path('loginUser/', LoginUser, name="loginUser"),
    path('AllUsers/', AllUsers, name="allUsers"),
    path('AddNewUser/',AddNewUser, name="addNewUser"),
]