from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from common.Helper import GetCurrentTime
from Admin.models import InternalProcess
from Admin.Serializers import InternalProcessSer
from Sales.models import clientDetails


# Create your views here.
class ProductionHomeClass(ListView):
    queryset = InternalProcess.objects.filter(process_id=2)
    template_name = 'ProductionHome.html'
    context_object_name = 'production_data'

    def get_context_data(self, **kwargs):
        context = super(ProductionHomeClass, self).get_context_data(**kwargs)
        data = InternalProcessSer(self.queryset, many=True)
        dataList = []
        for i in data.data:
            dataList.append(clientDetails.objects.filter(lead_id=i['lead_id']))
        
        context['client_details'] = dataList
        context['department'] = 'Production'

        return context