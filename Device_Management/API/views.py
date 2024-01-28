from rest_framework import generics
from Device.models import (
    Company, Employee, 
    Device, DeviceLog,
    DeviceLogReturn
)
from .serializers import (
    CompanySerializer, EmployeeSerializer, 
    DeviceSerializer, DeviceLogSerializer,
    DeviceLogReturnSerializer
)

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceLogListCreateView(generics.ListCreateAPIView):
    queryset = DeviceLog.objects.all()
    serializer_class = DeviceLogSerializer
    
class DeviceLogListReturnCreateView(generics.ListCreateAPIView):
    queryset = DeviceLogReturn.objects.all()
    serializer_class = DeviceLogReturnSerializer

