from rest_framework.serializers import ModelSerializer
from .models import ProductDetails, TwoMESP32, FourMESP32,\
                    SixMESP32, EightMESP32

# product serializer
class ProductDetailsSerializer(ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'


# 2M ESP 32
class TwoMESP32Ser(ModelSerializer):
    class Meta:
        model = TwoMESP32
        fields = '__all__'

# 4M ESP 32
class FourMESP32Ser(ModelSerializer):
    class Meta:
        model = FourMESP32
        fields = '__all__'


# 6M ESP 32
class SixMESP32Ser(ModelSerializer):
    class Meta:
        model = SixMESP32
        fields = '__all__'


# 8M ESP 32
class EightMESP32Ser(ModelSerializer):
    class Meta:
        model = EightMESP32
        fields = '__all__'