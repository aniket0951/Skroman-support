from rest_framework.serializers import ModelSerializer
from .models import LoginModel, InternalProcess


# Login model serializers
class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginModel
        fields = '__all__'

class InternalProcessSer(ModelSerializer):
    class Meta:
        model = InternalProcess
        fields = '__all__'        
