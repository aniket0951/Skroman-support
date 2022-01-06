from rest_framework import exceptions
import math
import random  
from django.core.mail import send_mail
from django.conf import settings
import smtplib

# -------- to check empty values or null point check -------------
def IsValidParam(param, request):
    if request is not None:
        if not param:
            return False
        else:
            return param, True
    else:
        return exceptions.NotFound("Please provide a validate param")

def SendOTP(email,request):
    otp = generateOTP()
    htmlgen = f"Your verification code is {otp}"
    send = send_mail('OTP request',otp,email,[email], fail_silently=False, html_message=htmlgen)
    if send:
        return True
    else:
        return False

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP