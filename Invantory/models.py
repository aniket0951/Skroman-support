from django.db import models

# Create your models here.

# 2M ESP 32 model for inventory
class TwoMESP32(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True)
    Quantity = models.CharField(max_length=1000, null=True, blank=True)
    Value = models.CharField(max_length=1000, null=True, blank=True)
    Pattern = models.CharField(max_length=1000, null=True, blank=True)
    RefDes = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = '2mesp32'