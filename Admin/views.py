from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from common.Helper import IsValidParam, SendOTP
from django.contrib import messages
import math
import random
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from .models import LoginModel
from .Serializers import LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json


# Create your views here.
def TestFun(request):
    loginStat = request.COOKIES.get('loginStatus')
    dep = request.COOKIES.get('department')

    if loginStat == "Login" and IsValidParam(dep, request):
        return navigateScreen(request, dep)
    else:
        return render(request, 'Login.html')


def LoginUser(request):
    email = request.GET.get('email')
    department = request.GET.get('department')
    otp = request.GET.get('otp')

    # check all params
    if IsValidParam(department, request) and IsValidParam(email, request):

        # check user is register or not
        user = LoginModel.objects.filter(email=email, department=department)

        if user:
            otp = generateOTP()
            if SendOTP(email, request, otp):
                login = LoginModel.objects.filter(email=email).update(user_otp=otp)
                messages.info(request, f"{email} {otp}")
                response = render(request, 'Verify.html')
                response.set_cookie('email', email)
                return response
            else:
                messages.error(request, "Failed to send a verification code please try again.")
                return render(request, 'Login.html')
        else:
            messages.error(request,
                           "Authentication Failed You Are Not A Authenticated User.Please Enter Correct Details")
            return render(request, 'LoginTemp.html')
    elif IsValidParam(otp, request):
        return VerifyOtp(request, otp)
    else:
        messages.error(request, "Please enter all details to login.")
        return render(request, 'LoginTemp.html')


def VerifyOtp(request, otp):
    email = request.COOKIES.get('email')
    login = LoginModel.objects.filter(email=email, user_otp=otp)
    serializer = LoginSerializer(login, many=True)
    if login:
        dep = serializer.data[0]['department']
        return navigateScreen(request, dep)
    else:
        return JsonResponse("User Authentication or otp verification failed", safe=False)


# generate the opt for verification
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


# check the department and navigate the screen by dep
def navigateScreen(request, department):
    if department == "Admin":
        response = render(request, 'MediaQ.html')
        response.set_cookie('loginStatus', "Login")
        response.set_cookie('department', department)
        return response
    elif department == "Inventory":
        pass


# all user list show and add new user
def AllUsers(request):
    return render(request, 'CreateUser.html')


# add new user department wise only authenticate for admin user
@csrf_exempt
def AddNewUser(request):
    employee_id = request.GET.get('employee_id')
    name = request.GET.get('name')
    email = request.GET.get('email')
    contact_no = request.GET.get('contact_no')
    designation = request.GET.get('designation')
    department = request.GET.get('department')

    auth_token = ''.join(random.choice('0123456789ABCDEF') for i in range(52))

    addNew = LoginModel.objects.create(employee_id=employee_id, name=name,
                                       email=email, contact_no=contact_no,
                                       designation=designation, department=department,
                                       auth_token=auth_token)

    if addNew:
        messages.success(request, "New User Created Successfully")
        return render(request, 'MediaQ.html')
    else:
        messages.error(request, "Faieled to create a new user . Please try again")
        return render(request, 'CreateUser.html')
