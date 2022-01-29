from rest_framework.serializers import ModelSerializer
from .models import *

# serializer for Production external process
class ProductionExternalSer(ModelSerializer):
    class Meta:
        model = ProductionExternalProcess
        fields = '__all__'