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


# for production user add/show
class ProductionUser(models.Model):
    emp_name = models.CharField(max_length=260, null=True, blank=True)
    emp_id = models.CharField(max_length=260, null=True, blank=True)
    emailId = models.CharField(max_length=260, null=True, blank=True)
    emp_contact = models.CharField(max_length=260, null=True, blank=True)
    designation = models.CharField(max_length=260, null=True, blank=True)
    department = models.CharField(max_length=260, null=True, blank=True)
    work_for = models.CharField(max_length=260, null=True, blank=True)
    emp_status = models.CharField(max_length=260, null=True, blank=True)
    password = models.CharField(max_length=140, null=True, blank=True)
    auth_token = models.CharField(max_length=140, null=True, blank=True)

    class Meta:
        db_table = 'production_user'

# to count a daily work or current day work how much task is assign
class WorkingCount(models.Model):
    auth_token = models.CharField(max_length=140, null=True, blank=True)
    working_date = models.CharField(max_length=140, null=True, blank=True)
    task_count = models.CharField(max_length=40, null=True, blank=True)
    device_id = models.CharField(max_length=120, null=True, blank=True)
    model = models.CharField(max_length=40, null=True, blank=True)
    model_name = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'working_count'

# for current working tasks
class CurrentWorkingTasks(models.Model):
    auth_token = models.CharField(max_length=140, null=True, blank=True)
    task_name = models.CharField(max_length=140, null=True, blank=True)
    task_id = models.CharField(max_length=140, null=True, blank=True)
    task_date = models.CharField(max_length=140, null=True, blank=True)
    task_status = models.CharField(max_length=10, null=True, blank=True)
    device_id = models.CharField(max_length=120, null=True, blank=True)
    model = models.CharField(max_length=40, null=True, blank=True)
    model_name = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'current_working_task'

# completed working task by production
class CompletedTask(models.Model):
    auth_token = models.CharField(max_length=140, null=True, blank=True)
    task_name = models.CharField(max_length=140, null=True, blank=True)
    task_id = models.CharField(max_length=140, null=True, blank=True)
    task_date = models.CharField(max_length=140, null=True, blank=True)
    task_status = models.CharField(max_length=10, null=True, blank=True)
    task_time = models.CharField(max_length=140, null=True, blank=True)
    device_id = models.CharField(max_length=120, null=True, blank=True)
    model = models.CharField(max_length=40, null=True, blank=True)
    model_name = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'completed_working_task'

# component to work for soldering
class SolderingWorkComponent(models.Model):
    model = models.CharField(max_length=40, null=True, blank=True)
    model_name = models.CharField(max_length=40, null=True, blank=True)
    pcb_type = models.CharField(max_length=260, null=True, blank=True)
    class Meta:
        db_table = 'soldering_work_component'