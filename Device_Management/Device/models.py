from django.db import models
from django.contrib.auth.models import User, AbstractUser


# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=255, unique=True) # name of user must be unique
#     email    = models.EmailField(unique=True) # email must be unique
    
#     def __str__(self) -> str:
#         return self.username

class Company(models.Model):
    name       = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at  = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name        = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['id']
    
    def __str__(self) -> str:
        return str(self.name)
    

class Employee(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    company    = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at  = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name        = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']
    
    def __str__(self) -> str:
        return str(self.user)
    

class Device(models.Model):
    name       = models.CharField(max_length=255)
    condition  = models.CharField(max_length=255) 
    created_at = models.DateTimeField(auto_now_add=True)
    modify_at  = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name        = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['id']
    
    def __str__(self) -> str:
        return str(self.name)
    

class DeviceLog(models.Model):
    id                      = models.IntegerField(primary_key=True, null=False, blank=False, unique=True)
    device                  = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee                = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_time          = models.DateTimeField()
    condition_when_out      = models.CharField(max_length=255)
    return_status           = models.BooleanField(default=False, null=True, blank=True)
    created_at              = models.DateTimeField(auto_now_add=True)
    modify_at               = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name        = 'Devicelog'
        verbose_name_plural = 'Devicelogs'
        ordering = ['id']
    
    def __str__(self) -> str:
        return str(self.device)
    
class DeviceLogReturn(models.Model):
    id                      = models.IntegerField(primary_key=True, null=False, blank=False, unique=True)
    device                  = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee                = models.ForeignKey(Employee, on_delete=models.CASCADE)
    return_time             = models.DateTimeField(null=True, blank=True)
    condition_when_returned = models.CharField(max_length=255, null=True, blank=True)
    return_status           = models.BooleanField(default=False, null=True, blank=True)
    created_at              = models.DateTimeField(auto_now_add=True)
    modify_at               = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name        = 'Devicelogreturn'
        verbose_name_plural = 'Devicelogreturns'
        ordering = ['id']
    
    def __str__(self) -> str:
        return str(self.device)

