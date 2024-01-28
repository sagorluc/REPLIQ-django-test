from django.contrib import admin
from django.contrib.auth.models import User
from Device.models import (Company, Device, 
                           DeviceLog, Employee, 
                           CustomUser, 
                           DeviceLogReturn
                        )

class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'username', 
        'email'
    ]
    ordering     = ['-id']

class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]    
    ordering     = ['id']
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'company',
    ]   
    ordering     = ['id']
    
class DeviceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'condition',
    ]   
    ordering     = ['id']
    
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'device',
        'employee',
        'check_out_time',        
        'condition_when_out',
        
    ]   
    ordering     = ['id']
    
class DeviceLogReturnAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'device',
        'employee',
        'return_time',        
        'condition_when_returned',
        
    ]   
    ordering     = ['id']
    

# Register all the admin  
admin.site.register(CustomUser, CustomUserAdmin)  
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceLog, DeviceLogAdmin)
admin.site.register(DeviceLogReturn, DeviceLogReturnAdmin)




