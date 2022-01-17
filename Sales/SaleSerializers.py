from rest_framework.serializers import ModelSerializer
from .models import leadDetails, clientDetails, clientProjectDetails,\
   leadReferances, leadStatus, leadNotes

# lead details serializer
class LeadDetailsSerializer(ModelSerializer):
    class Meta:
        model = leadDetails
        fields = '__all__'


# client details ser
class ClientDetailsSerializer(ModelSerializer):
    class Meta:
        model = clientDetails
        fields = '__all__'


# client project details
class ClientProjectDetailsSer(ModelSerializer):
    class Meta:
        model = clientProjectDetails
        fields = '__all__'


# lead referances ser
class LeadReferancesSerializer(ModelSerializer):
    class Meta:
        model = leadReferances
        fields = '__all__'

# lead status ser
class LeadStatus(ModelSerializer):
    class Meta:
        model = leadStatus
        fields = '__all__'

# lead notes
class LeadNotesSerializer(ModelSerializer):
    class Meta:
        model = leadNotes
        fields = '__all__'