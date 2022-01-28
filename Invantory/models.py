from django.db import models
from datetime import datetime, date

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

# 4M ESP 32 model for inventory
class FourMESP32(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True)
    Quantity = models.CharField(max_length=1000, null=True, blank=True)
    Value = models.CharField(max_length=1000, null=True, blank=True)
    Pattern = models.CharField(max_length=1000, null=True, blank=True)
    RefDes = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = '4MESP32'

# 6M ESP 32 model for inventory
class SixMESP32(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True)
    Quantity = models.CharField(max_length=1000, null=True, blank=True)
    Value = models.CharField(max_length=1000, null=True, blank=True)
    Pattern = models.CharField(max_length=1000, null=True, blank=True)
    RefDes = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = '6mesp32'

# 8M ESP 32 model for inventory
class EightMESP32(models.Model):
    Name = models.CharField(max_length=1000, null=True, blank=True)
    Quantity = models.CharField(max_length=1000, null=True, blank=True)
    Value = models.CharField(max_length=1000, null=True, blank=True)
    Pattern = models.CharField(max_length=1000, null=True, blank=True)
    RefDes = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = '8MESP32'

# product details when quatation is generated 
class ProductDetails(models.Model):
    device_type = models.CharField(max_length=210, null=True, blank=True)
    model_name = models.CharField(max_length=210, null=True, blank=True)
    quantity = models.CharField(max_length=210, null=True, blank=True)
    unit_price = models.CharField(max_length=210, null=True, blank=True)
    price = models.CharField(max_length=210, null=True, blank=True)
    lead_id = models.CharField(max_length=210, null=True, blank=True)
    client_name = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    bom_verification = models.CharField(max_length=210, null=True, blank=True)
    device_id = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        db_table = 'product_details'


# order details like all final prices of one order
class OrderDetails(models.Model):
    lead_id = models.CharField(max_length=210, null=True, blank=True)
    client_name = models.CharField(max_length=210, null=True, blank=True)
    sub_total = models.CharField(max_length=210, null=True, blank=True)
    discount = models.CharField(max_length=210, null=True, blank=True)
    final_price = models.CharField(max_length=210, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
    timestamp = models.CharField(max_length=210, null=True, blank=True)
    bom_verification = models.CharField(max_length=210, null=True, blank=True)

    class Meta:
        db_table = 'order_details'

# bom verification status manager
class BOMStatusManager(models.Model):
    verification_name = models.CharField(max_length=210, null=True, blank=True)
    verification_status = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'bom_status_manager'