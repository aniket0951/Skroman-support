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


# Create your views here.
def TestFun(request):
    return render(request, 'LoginTemp.html')

def LoginUser(request):
    email = request.GET.get('email')
    department = request.GET.get('department')

    # check all params
    if IsValidParam(department, request) and IsValidParam(email,request):
        
        # check user is register or not
        user = LoginModel.objects.filter(email=email, department=department)
        
        if user:
            messages.info(request,f"{email}")

            response = render(request, 'LoginTemp.html')
            response.set_cookie('email', email) 
            return response

            return render(request, 'LoginTemp.html')
            if SendOTP(email, request):
                messages.info(request,f"{email}")
                return render(request, 'LoginTemp.html')
            else:
                messages.error(request, "Failed to send a verification code please try again.")
                return render(request, 'LoginTemp.html')
        else:
            messages.error(request, "Authentication Failed You Are Not A Authenticated User.Please Enter Correct Details")
            return render(request,'LoginTemp.html')            
    else:
        messages.error(request, "Please enter all details to login.")
        return render(request,'LoginTemp.html')


def VerifyOtp(request):
    otp = request.GET.get('otp')
    print(otp)
    print(request.COOKIES.get('email'))
    return HttpResponse(email)     