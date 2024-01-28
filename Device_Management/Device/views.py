from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import (
    # CustomUser, 
    Company, Employee, 
    Device, DeviceLog, 
    DeviceLogReturn,
    CustomUser
)
from .forms import (
    CompanyForm, EmployeeForm, 
    DeviceForm, DeviceLogForm, 
    DeviceLogReturnForm,
    CustomUserForm
)
# Create your views here.

def create_user_view(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "User has been created successfully"    
            template = 'user_forms.html'
            return render(request, template, {'msg': msg})
        else:
            HttpResponse(request, 'Form is not valid')
            
    else:
        form = CustomUserForm()    
    template = 'user_forms.html'
    contex_data = {'forms': form}     
    return render(request, template, contex_data)

def show_all_data(request):
    all_obj = DeviceLog.objects.all()
    all_obj2 = DeviceLogReturn.objects.all()
    
    zipped_objs = zip(all_obj, all_obj2)
      
    context_data = {'all_objs_zip': zipped_objs, 'all_objs': all_obj, 'all_objs2': all_obj2}
    template = 'show_all_data.html'
    return render(request, template, context_data)

def company_view(request):
    form = CompanyForm()
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Company data has been created successfully"    
            template = 'company_forms.html'
            return render(request, template, {'msg': msg})
        else:
            HttpResponse(request, 'Form is not valid')
            
    else:
        form = CompanyForm()    
    template = 'company_forms.html'
    contex_data = {'forms': form}     
    return render(request, template, contex_data)

def employee_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Enployee data has been created successfully"
            template = 'employee_forms.html'
            return render(request, template, {'msg':msg})
        else:
            HttpResponse(request, 'Form is not valid')
            
    else:
        form = EmployeeForm() 
    msg = "Enployee data has been created successfully"    
    template = 'employee_forms.html'
    contex_data = {'forms': form,}     
    return render(request, template, contex_data)

def device_view(request):
    form = DeviceForm()
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Device data has been created successfully"
            template = 'device_forms.html'
            return render(request, template, {'msg':msg})
        else:
            HttpResponse(request, 'Form is not valid')
            
    else:
        form = DeviceForm()     
    template = 'device_forms.html'
    contex_data = {'forms': form}     
    return render(request, template, contex_data)

def devicelog_view(request):
    form = DeviceLogForm()
    if request.method == 'POST':
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "DeviceOut data has been created successfully"
            template = 'devicelog_forms.html'
            return render(request, template, {'msg':msg})
        else:
            HttpResponse(request, 'Form is not valid')
            
    else:
        form = DeviceLogForm()    
    template = 'devicelog_forms.html'
    contex_data = {'forms': form}      
    return render(request, template, contex_data)


def devicelogreturn_view(request):
    form = DeviceLogReturnForm()
    if request.method == 'POST':
        form = DeviceLogReturnForm(request.POST)
        if form.is_valid():
            input_id       = form.cleaned_data['id']
            input_device   = form.cleaned_data['device']
            input_employee = form.cleaned_data['employee']
            # print('#'*20, input_id, '#'*20)
            # print('#'*20, input_device, '#'*20)
            # print('#'*20, input_employee, '#'*20)
            is_correct = DeviceLog.objects.filter(
                id=input_id, device=input_device, 
                employee=input_employee, return_status=False
            )
            if is_correct:
                # data = form.save(commit=False)
                form.return_status = True
                form.save()
                msg = "Devicereturn data has been created successfully"
            else:
                msg = "Data does not match"
               
            template = 'devicelogreturn_forms.html'
            return render(request, template, {'msg':msg})
        else:
            HttpResponse(request, 'Form is not valid')
            
    else:
        form = DeviceLogReturnForm()    
    template = 'devicelogreturn_forms.html'
    contex_data = {'forms': form}      
    return render(request, template, contex_data)
            
            
