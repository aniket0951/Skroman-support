from rest_framework import exceptions
import math
import random  
from django.core.mail import send_mail
from django.conf import settings
import smtplib
import time

# -------- to check empty values or null point check -------------
def IsValidParam(param, request):
    if request is not None:
        if not param:
            return False
        else:
            return param, True
    else:
        return exceptions.NotFound("Please provide a validate param")

def SendOTP(email,request, otp):
    htmlgen = f"Your verification code is {otp}"
    send = send_mail('OTP request',otp,email,[email], fail_silently=False, html_message=htmlgen)
    if send:
        return True, otp
    else:
        return False

def GetCurrentTime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime
