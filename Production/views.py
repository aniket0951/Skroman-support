from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from common.Helper import GetCurrentTime
from Admin.models import InternalProcess
from Admin.Serializers import InternalProcessSer
from Sales.models import clientDetails
from .models import ProductionExternalProcess
from .ProductionSerializer import *
from Invantory.models import *
from Invantory.InventorySerializers import *
from common.Helper import *
from .models import *
from datetime import *

# Create your views here.
class ProductionHomeClass(ListView):
    queryset = ProductionExternalProcess.objects.all()
    template_name = 'ProductionHome.html'
    context_object_name = 'production_data'

    def get_context_data(self, **kwargs):
        context = super(ProductionHomeClass, self).get_context_data(**kwargs)
        data = ProductionExternalSer(self.queryset, many=True)
        dataList = []
        for i in data.data:
            dataList.append(clientDetails.objects.filter(lead_id=i['lead_id']))
        
        context['client_details'] = dataList
        context['department'] = 'Production'

        return context

# work on device by production head
def WorkOnDevice(request, lead_id, device_id):
    process = ProductionExternalProcess.objects.filter(device_id=device_id)
    process_ser = ProductionExternalSer(process, many=True)

    modelESP = process_ser.data[0]['model']

    # check here which process is pending and assign the work as Manager
    if process_ser.data[0]['bom_verification'] == '0':
        return DeviceBOMVerification(request, device_id, modelESP) 
    elif process_ser.data[0]['is_soldring'] == '0':
        return AssignSoldering(request, device_id)
    elif process_ser.data[0]['is_visual_inspection'] == '0':
        return AssignInspection(request, device_id)
    elif process_ser.data[0]['is_programing'] == '0':
        return AssignProgramming(request, device_id)
    elif process_ser.data[0]['is_testing'] == '0':
        return AssignTesting(request, device_id)
    elif process_ser.data[0]['is_f_testing'] == '0':
        return AssignFinalTesting(request, device_id)
    else:
        messages.info(request, "failed to find the pending work. please update the all work process")
        return redirect('/productionUser/productionHome') 

    return JsonResponse(f"{lead_id}, {device_id}", safe=False)

# verify the device bom by model wise
def DeviceBOMVerification(request, device_id, modelESP):
    context = {'bom_data': '', 'device_id': device_id}
    
    # check which model type is selected divice and render as BOM data
    if modelESP == '2M':
        twoMESP32 = TwoMESP32.objects.all()
        twoMESP32Ser = TwoMESP32Ser(twoMESP32, many=True)
        context.update({'bom_data' : twoMESP32Ser.data})
    
    elif modelESP == '4M':
        fourMESP32 = FourMESP32.objects.all()
        fourMESP32Ser = FourMESP32Ser(fourMESP32, many=True)
        context.update({'bom_data': fourMESP32Ser.data})
    
    elif modelESP == '6M':
        sixMESP32 = SixMESP32.objects.all()
        sixMESP32Ser = SixMESP32Ser(sixMESP32, many=True)
        context.update({'bom_data':sixMESP32Ser.data})
    
    elif modelESP == '8M':
        eightMESP32 = EightMESP32.objects.all()
        eightMESP32Ser = EightMESP32Ser(eightMESP32, many=True)
        context.update({'bom_data': eightMESP32Ser.data})        

    return render(request, 'ProductionBOM.html', context)
    


# assign the soldering work for soldering person
def AssignSoldering(request, device_id):
    return AssignAlgorithm(request, 'Soldering', device_id)

# assign the work for visual inspection person
def AssignInspection(request, device_id):
    return JsonResponse("from visual inspection", safe=False)


# assing the work for device programing
def AssignProgramming(request, device_id):
    return AssignAlgorithm(request, 'Programming', device_id)

# assing the work for testing person
def AssignTesting(request, device_id):
    return JsonResponse("from testing", safe=False)

# assign the work for final testing person
def AssignFinalTesting(request, device_id):
    return JsonResponse("from final testing", safe=False)


# Assign task algorithm for all process like programing, soldering , testing etc
def AssignAlgorithm(request, work_for,device_id):
    currentdate = date.today()
    users = ProductionUser.objects.filter(work_for=work_for)
    user_ser = ProductionUserSer(users, many=True)

    # get device detail from production external details
    device = ProductionExternalProcess.objects.filter(device_id=device_id)
    device_ser = ProductionExternalSer(device, many=True)
    model = ""
    model_name = ""
    if device:
        model = device_ser.data[0]['model']
        model_name = device_ser.data[0]['model_name']
    else:
        messages.error(request, "Failed to assign this task please try again after sometime")
        return redirect('/productionUser/productionHome/')    

    # store first all auth_tokens here if need assign random task
    auth_tokens = []
    for i in user_ser.data:
        auth_tokens.append(i['auth_token'])

    # to store the count and auth token using dict
    count_dict = {}

    # check if how much work count is assign
    for i in auth_tokens:
        token = i
        # check the auth token is present or not here
        if WorkingCount.objects.filter(auth_token=token, working_date=currentdate).exists():
            
            work_count = WorkingCount.objects. filter(auth_token=i)
            work_count_ser = WorkingCountSer(work_count, many=True)
            count_dict[token] = work_count_ser.data[0]['task_count']
                        
        else:
            addWork = WorkingCount(auth_token=token, working_date=currentdate, task_count=1, device_id=device_id,
                                   model=model, model_name=model_name).save()
            messages.success(request, "Soldering Assign Successfully")
            return redirect('/productionUser/productionHome/')
    
    # get minimum work count here
    countList = list(count_dict.values())
    last_count = int(countList[0])
    for i in range(len(countList)):
        curMin = int(countList[i])
        last_count = min(last_count, curMin)
    
    # check which user has a minimum count and assign task
    for i,j in count_dict.items():
        if j == str(last_count):
            last_count += 1
            # update working task count 
            addCount = WorkingCount.objects.filter(auth_token=i).update(task_count=last_count)
            
            # get a user name to show a admin user
            users = ProductionUser.objects.filter(auth_token=i)
            user_ser = ProductionUserSer(users, many=True)

            name = user_ser.data[0]['emp_name']

            # assign current working task
            task_id = GetAlphNumerical(10)
            currentTask = CurrentWorkingTasks(auth_token=i, task_name="Soldering",
                                              task_id=task_id,task_date=currentdate,
                                              task_status=0, device_id=device_id, model=model,
                                              model_name=model_name).save()
            messages.success(request, f"{work_for} task assign to {name}")
            return redirect('/productionUser/productionHome/')                                  

    messages.error(request, "Failed to assign a soldering task. please try after some time")
    return redirect('/productionUser/productionHome/')                                  


# verify the bom of selected device 
def BomVerification(request, device_id):
    # verify bom and update verification status
    verify = ProductionExternalProcess.objects.filter(device_id=device_id).update(bom_verification=1)

    messages.success(request, f"Bom Verification Successfull of the divice id is, {device_id}")
    return redirect('/productionUser/productionHome')

# show all production users and add new user in production
def ProductionUsers(request, tag):
    if tag == 'add':
        emp_name = request.GET.get('emp_name')
        emailId = request.GET.get('email')
        emp_contact = request.GET.get('emp_contact')
        designation = request.GET.get('designation')
        work_for = request.GET.get('work_for')
        department = 'Production'
        emp_status = 'Active'
        password = request.GET.get('password')
        auth_token = request.GET.get('auth_token')
        number = GenerateRandom(4)
        emp_id = f"emp_{number}"

        # check if auth token is empty then generate new token

        if auth_token == 'empty':
            auth_token = GetAlphNumerical(52)
            members = ProductionUser(emp_name=emp_name,emp_id=emp_id,
                                 emailId=emailId,emp_contact=emp_contact,
                                 designation=designation,department=department,
                                 work_for=work_for,emp_status=emp_status,
                                 password=password, auth_token=auth_token).save()
        else:
            update_data = ProductionUser.objects.filter(auth_token=auth_token).update(emp_name=emp_name,emp_id=emp_id,
                                 emailId=emailId,emp_contact=emp_contact,
                                 designation=designation,department=department,
                                 work_for=work_for,emp_status=emp_status,
                                 password=password, auth_token=auth_token)

        
            
      
        messages.success(request, "New member add in production successfully")
        return redirect('/productionUser/ProductionUser/show/')
    

    elif tag == 'show':
        # get all members here
        production = ProductionUser.objects.all()
        productionSer = ProductionUserSer(production, many=True)

        context = {}
        context['department'] = 'Production'
        context['production_members'] = productionSer.data
        return render(request, 'ProductionUsers.html', context)


# get production members daily tasks
def DailyTasks(request, auth_token):
    tasks = CurrentWorkingTasks.objects.filter(auth_token=auth_token)

    if tasks:
        task_ser = CurrentWorkingTasksSer(tasks, many=True)
        for i in task_ser.data:
            model_name = i['model_name']
            if model_name:
                # get pcb type from model name
                component = SolderingWorkComponent.objects.filter(model_name=model_name)
                component_ser = SolderingWorkCompSer(component, many=True)
                i['pcb_types'] = component_ser.data[0]['pcb_type']
         
        context = {
            'daily_task' : task_ser.data
        }
        return render(request, 'ProductionMembersHome.html', context)
    else:
        return HttpResponse('Not a assign any task')    

def TestFunction(request):
    time = request.GET.get('timer')
    return HttpResponse(f"Test function run from view {time}")
