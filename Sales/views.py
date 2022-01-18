from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import leadDetails, clientDetails, leadReferances, clientProjectDetails,leadNotes
from .SaleSerializers import LeadDetailsSerializer, ClientDetailsSerializer,\
                LeadReferancesSerializer, ClientProjectDetailsSer, LeadNotesSerializer
import random
from django.contrib import messages
import datetime
import time
from django.views.decorators.csrf import csrf_exempt
from common.Helper import GetCurrentTime


# Create your views here.
# show sales depart home screen
def TestFun(request):
    clientData = clientDetails.objects.all()
    client_seri = ClientDetailsSerializer(clientData, many=True)

    context = {
        'client_data': client_seri.data
    }
    return render(request, 'SalesHome.html', context)

def addNewClient(request, tag):
    if tag == "show":
        return render(request, 'AddNewClient.html')
    elif tag == 'add':
        c_type = request.GET.get('client_type')
        c_name = request.GET.get('c_name')
        c_email = request.GET.get('c_email')
        c_mobile = request.GET.get('c_mobile')
        c_address = request.GET.get('c_address')
        c_site_address = request.GET.get('c_site_address')
        localtime = GetCurrentTime()

        # generating lead id
        lead_id = ''.join(random.choice('0123456789ABCDEF') for i in range(4))
        lead_id = f"client_{lead_id}"
        addClient = clientDetails.objects.create(c_name=c_name,c_email=c_email, c_mobile=c_mobile,
                                                 c_address=c_address, c_site_address=c_site_address,
                                                 c_type=c_type,lead_id=lead_id, lead_status=1,ctime=localtime,
                                                 timestamp=localtime)
        if addClient:
            return addLeadReferance(request, lead_id)
        else:
            messages.error(request, "Failed to add new client please try again")
            return render(request, 'SalesHome.html')                                             
        
    else:
        return JsonResponse("Add new client called ", safe=False)   

# add all lead referance details
def addLeadReferance(request,lead_id):
    referal = request.GET.get('referal', 'default')
    ref_type = request.GET.get('ref_type', 'default')
    ref_name = request.GET.get('ref_name')
    ref_number = request.GET.get('ref_number')
    ref_email = request.GET.get('ref_email')
    ref_address = request.GET.get('ref_address')
    ct = datetime.datetime.now()
    localtime = GetCurrentTime()


    if referal == "IsReferal":
        addRefence = leadReferances.objects.create(lead_id=lead_id,ref_type=ref_type,ref_name=ref_name,
                                                   ref_mobile=ref_number,ref_email=ref_email,ref_address=ref_address,
                                                   lead_status=1, ctime=ct, uptime=ct, timestamp=localtime)
        if addRefence:
            return addProjectDetails(request, lead_id)
        else:
            messages.error(request, "Failed to add a lead referances please try again")
            return render(request, 'AddNewClient.html')
    else:
        return addProjectDetails(request, lead_id)                                                       

# add project details if client have a project
def addProjectDetails(request,lead_id):
    leadFor = request.GET.get('leadFor','default')
    p_name = request.GET.get('p_name')
    p_site_number = request.GET.get('p_site_number')
    p_address = request.GET.get('p_address')
    ct = datetime.datetime.now()
    localtime = GetCurrentTime()

    if leadFor == "Project":
        addProDetail = clientProjectDetails.objects.create(lead_id=lead_id,project_name=p_name, site_number=p_site_number,
                                                           project_address=p_address,lead_status=1,ctime=ct, uptime=ct,
                                                           timestamp=localtime)
        if addProDetail:
            messages.success(request, 'Client details added successfully')
            return render(request, 'SalesHome.html')
        else:
            messages.error(request, "Failed to add a Project details.Please update the project details")
            return render(request, 'SalesHome.html')
    else:
        messages.error(request, "Failed to add a Project details.Please update the project details")
        return render(request, 'SalesHome.html')                                   


# edit client details
def editClientDetails(request, tag, lead_id):
    # return JsonResponse(lead_id, safe=False)
    if tag == "show":
        clientData = clientDetails.objects.filter(lead_id=lead_id)
        client_seri = ClientDetailsSerializer(clientData, many=True)

        c_pro_data = clientProjectDetails.objects.filter(lead_id=lead_id)
        c_pro_ser = ClientProjectDetailsSer(c_pro_data, many=True)

        # getting old notes data
        note_data = leadNotes.objects.filter(lead_id=lead_id)
        note_ser = LeadNotesSerializer(note_data, many=True)
        context = {
            'client_data': client_seri.data,
            'project_data' : c_pro_ser.data,
            'note_data' : note_ser.data
        }
        return render(request, 'EditLead.html', context)
    elif tag == "edit":
        # get value of client info 
        c_name = request.GET.get('c_name')
        c_email = request.GET.get('c_email')
        c_mobile = request.GET.get('c_mobile')
        c_address = request.GET.get('c_address')
        c_site_address = request.GET.get('c_site_address')
        localtime = time.asctime(time.localtime(time.time()))

        # get value of production info
        p_name = request.GET.get('p_name')
        p_site_number = request.GET.get('p_site_number')
        p_address = request.GET.get('p_address')
        ct = datetime.datetime.now()
        localtime = time.asctime(time.localtime(time.time()))

        clientData = clientDetails.objects.filter(lead_id=lead_id).update(c_name=c_name, c_email=c_email,
                                                  c_mobile=c_mobile,c_address=c_address,
                                                  c_site_address=c_site_address,
                                                  timestamp=localtime)
        
        c_pro_data = clientProjectDetails.objects.filter(lead_id=lead_id).update(project_name=p_name,site_number=p_site_number,
                                                                                 project_address=p_address,timestamp=localtime)

        if clientData and c_pro_data:
            return JsonResponse(c_name, safe=False)
        else:
            return JsonResponse("Failed to update", safe=False)    
    else:
        return JsonResponse("Edit client details called", safe=False)

# delete a lead 
def deleteLead(request, lead_id, tag):
    if tag == 'delete':
        del_client = clientDetails.objects.get(lead_id=lead_id)
        del_lead_ref = leadReferances.objects.get(lead_id=lead_id)
        del_proj_details = clientProjectDetails.objects.get(lead_id=lead_id)

        del_client.delete()
        del_lead_ref.delete()
        del_proj_details.delete()

        messages.success(request, "Lead Deleted Successfully")
        return render(request, 'SalesHome.html')
    elif tag == "conform":
        clientData = clientDetails.objects.all()
        cliet_seri = ClientDetailsSerializer(clientData, many=True)
        messages.info(request, "info")
        return render(request, 'SalesHome.html', {'lead_id': lead_id, 'client_data': cliet_seri.data})
    else:
        return JsonResponse(f"not a post method {lead_id}", safe=False)

@csrf_exempt
def addLeadNote(request, lead_id):
    note = request.GET.get('comment')
    next_follow = request.GET.get('next_follow')
    tied_up_date = request.GET.get('tied_up_date')
    isOrderConform = request.GET.get('isOrderConform', 'default')
    time = GetCurrentTime()

    temp_lead = ""

    if isOrderConform == 'conform':
        temp_lead = "2"
    else:
        temp_lead = "1"
    

    note_data = leadNotes(lead_id=lead_id, note=note, next_follow=next_follow,
                          tied_up_date=tied_up_date, timestamp=time)                      
    
    note_data.save()                    
    if note_data:
        leadNotes.objects.filter(lead_id=lead_id).update(lead_status=temp_lead)
        clientDetails.objects.filter(lead_id=lead_id).update(lead_status=temp_lead)
        
        messages.success(request, 'Note added successfully')
        return render(request, 'SalesHome.html')
    else:
        return JsonResponse("Not a valid response", safe=False)    