from django.db import models
from datetime import datetime, date

# Create your models here.
class leadDetails(models.Model):
    lead_id = models.CharField(max_length=120, null=True, blank=True)
    lead_status = models.CharField(max_length=10, null=True, blank=True)
    status_code = models.CharField(max_length=10, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=60, null=True, blank=True)


    class Meta:
        db_table = 'lead_details'

# client details model
class clientDetails(models.Model):
    c_name = models.CharField(max_length=460, null=True, blank=True)
    c_email = models.CharField(max_length=230, null=True, blank=True)
    c_address = models.CharField(max_length=460, null=True, blank=True)
    c_mobile = models.CharField(max_length=10, null=True, blank=True)
    c_type = models.CharField(max_length=40, null=True, blank=True)
    c_site_address = models.CharField(max_length=460, null=True, blank=True)
    client_status = models.CharField(max_length=40, null=True, blank=True)
    lead_id = models.CharField(max_length=20, null=True, blank=True)
    lead_status = models.CharField(max_length=20, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'client_details'

# client project details
class clientProjectDetails(models.Model):
    lead_id = models.CharField(max_length=20, null=True, blank=True)
    project_name = models.CharField(max_length=110, null=True, blank=True)
    site_number = models.CharField(max_length=10, null=True, blank=True)
    project_address = models.CharField(max_length=460, null=True, blank=True)
    lead_status = models.CharField(max_length=40, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'client_project_details'

# lead referances
class leadReferances(models.Model):
    lead_id = models.CharField(max_length=20, null=True, blank=True)
    ref_name = models.CharField(max_length=160, null=True, blank=True)
    ref_mobile =  models.CharField(max_length=10, null=True, blank=True)
    ref_email = models.CharField(max_length=140, null=True, blank=True)
    ref_address = models.CharField(max_length=460, null=True, blank=True)
    lead_status = models.CharField(max_length=40, null=True, blank=True)
    ref_type = models.CharField(max_length=40, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        db_table = 'lead_referances'

# lead status
class leadStatus(models.Model):
    lead_name = models.CharField(max_length=40, null=True, blank=True)
    status_code = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'lead_status'

# lead notes when lead is generate
class leadNotes(models.Model):
    id = models.AutoField(primary_key=True)
    lead_id = models.CharField(max_length=120, null=True, blank=True)
    note = models.CharField(max_length=4450, null=True,blank=True)
    next_follow = models.CharField(max_length=150, null=True,blank=True)
    tied_up_date = models.CharField(max_length=150, null=True,blank=True)
    lead_status = models.CharField(max_length=50, null=True,blank=True)
    timestamp = models.CharField(max_length=150, null=True,blank=True) 

    class Meta:
        db_table = 'lead_notes'