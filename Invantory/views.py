from django.shortcuts import render, redirect
from Admin.models import InternalProcess
from Sales.models import clientDetails
from django.views.generic.list import ListView
from Admin.Serializers import InternalProcessSer
from .models import TwoMESP32, FourMESP32, SixMESP32, EightMESP32, ProductDetails
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .InventorySerializers import ProductDetailsSerializer, TwoMESP32Ser, FourMESP32Ser, SixMESP32Ser,\
                                  EightMESP32Ser 
from common.Helper import GetCurrentTime


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

class BOMListClass(ListView):
    model = TwoMESP32
    template_name = "BOM.html"
    context_object_name = 'bom_data'

    def get_context_data(self, **kwargs):
        context = super(BOMListClass, self).get_context_data(**kwargs)
        forMESP32 = FourMESP32.objects.all()
        sixMESP32 = SixMESP32.objects.all()
        eightMESP32 = EightMESP32.objects.all()

        context['4MESP32'] = forMESP32
        context['6MESP32'] = sixMESP32
        context['8MESP32'] = eightMESP32

        return context

# add new component in bom list by device type
def AddBOM(request):
    c_name = request.GET.get('c_name')
    quantity = request.GET.get('quantity')
    c_value = request.GET.get('c_value')
    pattern = request.GET.get('pattern')
    ref_des = request.GET.get('ref_des')
    device_type = request.GET.get('device_type')
    
    # check device type 
    if device_type == '2MESP32':
        twoMESP32 = TwoMESP32(Name=c_name,Quantity=quantity, Value=c_value,
                              Pattern=pattern,RefDes=ref_des).save()

        return BOMAddValidation(request, 'success')
    elif device_type == '4MESP32':
        forMESP32 = FourMESP32(Name=c_name,Quantity=quantity, Value=c_value,
                              Pattern=pattern,RefDes=ref_des).save()
        return BOMAddValidation(request, 'success')
    elif device_type == '6MESP32':
        sixMESP32 = SixMESP32(Name=c_name,Quantity=quantity, Value=c_value,
                              Pattern=pattern,RefDes=ref_des).save()
        return BOMAddValidation(request, 'success')
    elif device_type == '8MESP32':
        eightMESP32 = EightMESP32(Name=c_name,Quantity=quantity, Value=c_value,
                              Pattern=pattern,RefDes=ref_des).save()
        return BOMAddValidation(request, 'success')         
    else:
        return BOMAddValidation(request,'error')                        

# check component added or not in bom  
def BOMAddValidation(request,tag):
    if tag == 'success':
        messages.success(request,'Component Added Successfully')
        return redirect('/invantoryUser/invantoryHome/')
    if  tag == 'error':
        messages.error(request, 'Failed to add a component to BOM . Please try again')
        return redirect('/invantoryUser/invantoryHome/')


# bom verification
def BOMVerification(request, tag, lead_id):
    if tag == 'show':
        product = ProductDetails.objects.filter(lead_id=lead_id)
        data = ProductDetailsSerializer(product, many=True)

        context = {
            'verification_data' : data.data
        }

        return render(request, 'BomVerification.html', context)
    elif tag == 'verify':

        # here lead_id acts as a device id here
        verify = ProductDetails.objects.filter(device_id=lead_id).update(bom_verification=1)

        # get lead_id from device_id
        data = ProductDetails.objects.filter(device_id=lead_id)
        dataSer = ProductDetailsSerializer(data, many=True)

        new_lead_id = dataSer.data[0]['lead_id']

        return BOMVerification(request, 'show', new_lead_id)  
   
# show all devices component quantity and another information
def showComponentInfo(request, model_name, quantity, device_id):

    # get a device information from device_id
    device = ProductDetails.objects.filter(device_id=device_id)
    devices = ProductDetailsSerializer(device, many=True)
    
    
    quantity = int(quantity)

    # check which model for device have
    if model_name == '2M':
        twoMESP32 = TwoMESP32.objects.all()
        data = TwoMESP32Ser(twoMESP32, many=True)      
    elif model_name == '4M':
        fourMESP32 = FourMESP32.objects.all()
        data = FourMESP32Ser(fourMESP32, many=True)

    for i in data.data:
        i['data_quantity'] = (int(float(i['Quantity'])) * quantity)

    context = {
        'bom_data':data.data,
        'device_data' : devices.data
    }
    messages.info(request, 'show bom data')    
    return render(request, 'BomVerification.html', context)


# proceed to production a lead check all bom Verification is done
def ProceedProduction(request, lead_id):
    
    # first check all device bom is verified
    bom = ProductDetails.objects.filter(lead_id=lead_id)
    bomSer = ProductDetailsSerializer(bom, many=True)

    for i in bomSer.data:
        if i['bom_verification'] == '0':
            messages.error(request, "BOM Verification is Pending Please verify all bom list.")
            return redirect('/invantoryUser/invantoryHome/')

    time = GetCurrentTime()        

    # if all bom list is verified then change the internal process status
    internal_pro = InternalProcess.objects.filter(lead_id=lead_id).update(dept_name="Production",
                                                                          dept_id=3, process_id=2,
                                                                          process_name='In Production',
                                                                          timestamp=time)

    if internal_pro:
        messages.success(request, "Lead proceed to production successfully")        
        return redirect('/invantoryUser/invantoryHome/')
    else:
        messages.error(request, "Failed to proceed lead to production. Please try again")
        return redirect('/invantoryUser/invantoryHome/')        