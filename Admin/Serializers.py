from rest_framework.serializers import ModelSerializer
from .models import LoginModel


# Login model serializers
class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginModel
        fields = '__all__'
