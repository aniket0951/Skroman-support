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


# Create your views here.
def TestFun(request):
    return render(request, 'LoginTemp.html')


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
                response = render(request, 'LoginTemp.html')
                response.set_cookie('email', email)
                return response
            else:
                messages.error(request, "Failed to send a verification code please try again.")
                return render(request, 'LoginTemp.html')
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
        return HttpResponse(f"your otp is {otp} and email is {email}")
    else:
        return JsonResponse("User Authentication or otp verification failed", safe=False)


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
