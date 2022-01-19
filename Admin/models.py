from django.db import models
from datetime import datetime, date


# Create your models here.
class LoginModel(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    designation = models.CharField(max_length=120, null=True, blank=True)
    department = models.CharField(max_length=120, null=True, blank=True)
    employee_id = models.CharField(max_length=120, null=True, blank=True)
    contact_no = models.CharField(max_length=120, null=True, blank=True)
    auth_token = models.CharField(max_length=120, null=True, blank=True)
    user_otp = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "skroman_login"

# creating a common model class to track internal process
class InternalProcess(models.Model):
    dept_name = models.CharField(max_length=120, null=True, blank=True)
    dept_id = models.CharField(max_length=120, null=True, blank=True)
    lead_id = models.CharField(max_length=120, null=True, blank=True)
    process_id = models.CharField(max_length=120, null=True, blank=True)
    process_name = models.CharField(max_length=120, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=120, null=True, blank=True)
    
    class Meta:
        db_table = "internal_process"

# internal process id and process names
class ProcessDescription(models.Model):
    process_id = models.CharField(max_length=120, null=True, blank=True)
    process_name = models.CharField(max_length=120, null=True, blank=True)
    dept_name = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "process_description"

# department name and department id
class Departments(models.Model):
    dept_name = models.CharField(max_length=120, null=True, blank=True)
    dept_id = models.CharField(max_length=120, null=True, blank=True)
    dept_head = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "departments" 