from django import forms
from datetime import timezone
from django.contrib.auth.models import User
from .models import (
    Company, Employee, 
    Device, DeviceLog, 
    # CustomUser, 
    DeviceLogReturn
)
class CompanyForm(forms.ModelForm):
    class  Meta:
        model = Company
        fields = ['name']        
        labels = {
           'name' : 'Name of company'
        }
              
    # set placeholder by overriding    
    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter the name of company'

        
class EmployeeForm(forms.ModelForm):
    class  Meta:
        model = Employee
        fields = ['user', 'company']   
        labels = {
           'user'    : 'Name of staff',
           'company'       : 'Name of company',
        }
               
    # set placeholder by overriding    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['placeholder']    = 'Enter the name of staff'
        self.fields['company'].widget.attrs['placeholder'] = 'Enter staff company'

 
class DeviceForm(forms.ModelForm):
    class  Meta:
        model = Device
        fields = ['name', 'condition']       
        labels = {
           'name'      : 'Device Name',
           'condition' : 'Device Condition'
        }
        
    # set placeholder by overriding    
    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']      = 'Enter the name of device'
        self.fields['condition'].widget.attrs['placeholder'] = 'Enter the condition of device'
        

class DeviceLogForm(forms.ModelForm):
    class  Meta:
        model = DeviceLog
        fields = [
            'id',
            'device', 
            'employee', 
            'check_out_time',            
            'condition_when_out', 
        ]       
        labels = {
           'id'                      : 'Id number',
           'device'                  : 'Name of device',
           'employee'                : 'Name of employee',
           'check_out_time'          : 'Time of checkout',           
           'condition_when_out'      : 'Conditon of outing',
           
        }
        
        # set calender of date and time
        widgets = {
            'check_out_time': forms.DateInput(attrs={'type': 'datetime-local'}),            
        }
        
    # set placeholder by overriding    
    def __init__(self, *args, **kwargs):
        super(DeviceLogForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['placeholder']                     = 'Enter an id'
        self.fields['device'].widget.attrs['placeholder']                 = 'Enter the name of device'
        self.fields['employee'].widget.attrs['placeholder']               = 'Enter the name of employee'
        self.fields['check_out_time'].widget.attrs['placeholder']         = 'Enter check out time'  
        self.fields['condition_when_out'].widget.attrs['placeholder']     = 'Enter the conditon of device when out'
       
        
        
class DeviceLogReturnForm(forms.ModelForm):
    class  Meta:
        model = DeviceLogReturn
        fields = [
            'id',
            'device', 
            'employee', 
            'return_time',  
            'condition_when_returned',
            'return_status', 
        ]
               
        labels = {
           'id'                      : 'Id number',
           'device'                  : 'Name of device',
           'employee'                : 'Name of employee',
           'return_time'             : 'Time of return',
           'condition_when_returned' : 'Condition of returning',
           'return_status'           : 'Is returning',
        }
        
        # set calender of date and time
        widgets = {
            'return_time'  : forms.TimeInput(attrs={'type': 'datetime-local'}),
            'return_status': forms.CheckboxInput(attrs={'type': 'checkbox'}),
            
        }
        
    # set placeholder by overriding    
    def __init__(self, *args, **kwargs):
        super(DeviceLogReturnForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['placeholder']                      = 'Enter the correct id number'
        self.fields['device'].widget.attrs['placeholder']                  = 'Enter the name of device'
        self.fields['employee'].widget.attrs['placeholder']                = 'Enter the name of employee'
        self.fields['return_time'].widget.attrs['placeholder']             = 'Enter return time'
        self.fields['condition_when_returned'].widget.attrs['placeholder'] = 'Enter the condition of device when return'

    