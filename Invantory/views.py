from django.shortcuts import render
from Admin.models import InternalProcess
from Sales.models import clientDetails
from django.views.generic.list import ListView
from Admin.Serializers import InternalProcessSer

# Create your views here.
class InvantoryHomeClass(ListView):
    queryset = InternalProcess.objects.all()
    template_name = 'InvantoryHome.html'
    context_object_name = 'invantory_data'

    def get_context_data(self, **kwargs):
        context = super(InvantoryHomeClass, self).get_context_data(**kwargs)
        data = InternalProcessSer(self.queryset, many=True)
        dataList = []
        for i in data.data:
            dataList.append(clientDetails.objects.filter(lead_id=i['lead_id']))
        
        context['client_details'] = dataList
            
        return context

