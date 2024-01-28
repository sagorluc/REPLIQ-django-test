from django.urls import path
from .views import (
    CompanyListCreateView, EmployeeListCreateView, 
    DeviceListCreateView, DeviceLogListCreateView,
    DeviceLogListReturnCreateView
)

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('device-logs/', DeviceLogListCreateView.as_view(), name='device-log-list-create'),
    path('device-logs-return/', DeviceLogListReturnCreateView.as_view(), name='device-log-return-list-create'),
]
