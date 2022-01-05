from django.db import models


# Create your models here.
class LoginModel(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    email = models.CharField(max_length=120, null=True, blank=True)
    designation = models.CharField(max_length=120, null=True, blank=True)
    department = models.CharField(max_length=120, null=True, blank=True)
    employee_id = models.CharField(max_length=120, null=True, blank=True)
    contact_no = models.CharField(max_length=120, null=True, blank=True)
    auth_token = models.CharField(max_length=120, null=True, blank=True)
    status = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = "skroman_login"
