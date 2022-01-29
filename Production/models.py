from django.db import models
from datetime import datetime, date

# Create your models here.

# create first production external process model
class ProductionExternalProcess(models.Model):
    lead_id = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=210, null=True, blank=True)
    bom_verification = models.CharField(max_length=210, null=True, blank=True)
    is_soldring = models.CharField(max_length=210, null=True, blank=True)
    is_visual_inspection = models.CharField(max_length=210, null=True, blank=True)
    is_programing = models.CharField(max_length=210, null=True, blank=True)
    is_testing = models.CharField(max_length=210, null=True, blank=True)
    is_f_testing = models.CharField(max_length=210, null=True, blank=True)
    model = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'production_external_process'


# from here define all internal process model

class Soldering(models.Model):
    model = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    pcb_type = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=210, null=True, blank=True)
    soldering_time = models.CharField(max_length=210, null=True, blank=True)
    soldering_by = models.CharField(max_length=210, null=True, blank=True)
    user_auth_token = models.CharField(max_length=210, null=True, blank=True)
    soldering_status = models.CharField(max_length=210, null=True, blank=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'production_soldering'

class VisualInspection(models.Model):
    model = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    pcb_type = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=210, null=True, blank=True)
    inspection_time = models.CharField(max_length=210, null=True, blank=True)
    inspection_by = models.CharField(max_length=210, null=True, blank=True)
    user_auth_token = models.CharField(max_length=210, null=True, blank=True)
    inspection_status = models.CharField(max_length=210, null=True, blank=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'production_visual_inspection'

class Programing(models.Model):
    model = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    pcb_type = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=210, null=True, blank=True)
    programing_time = models.CharField(max_length=210, null=True, blank=True)
    programing_by = models.CharField(max_length=210, null=True, blank=True)
    user_auth_token = models.CharField(max_length=210, null=True, blank=True)
    programing_status = models.CharField(max_length=210, null=True, blank=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'production_programing'


class Tetsing(models.Model):
    model = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    pcb_type = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=210, null=True, blank=True)
    testing_time = models.CharField(max_length=210, null=True, blank=True)
    testing_by = models.CharField(max_length=210, null=True, blank=True)
    user_auth_token = models.CharField(max_length=210, null=True, blank=True)
    testing_status = models.CharField(max_length=210, null=True, blank=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'production_testing'

class FinalTesting(models.Model):
    model = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    pcb_type = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=210, null=True, blank=True)
    f_testing_time = models.CharField(max_length=210, null=True, blank=True)
    f_testing_by = models.CharField(max_length=210, null=True, blank=True)
    user_auth_token = models.CharField(max_length=210, null=True, blank=True)
    f_testing_status = models.CharField(max_length=210, null=True, blank=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'production_final_testing'