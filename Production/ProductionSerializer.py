from rest_framework.serializers import ModelSerializer
from .models import *

# serializer for Production external process
class ProductionExternalSer(ModelSerializer):
    class Meta:
        model = ProductionExternalProcess
        fields = '__all__'


# production users/members here
class ProductionUserSer(ModelSerializer):
    class Meta:
        model = ProductionUser
        fields = '__all__'

# working count serializer
class WorkingCountSer(ModelSerializer):
    class Meta:
        model = WorkingCount
        fields = '__all__'


# working tasks serializers
class CurrentWorkingTasksSer(ModelSerializer):
    class Meta:
        model = CurrentWorkingTasks
        fields = '__all__'

# work completed task ser
class CompletedTaskSer(ModelSerializer):
    class Meta:
        model = CompletedTask
        fields = '__all__'