from django.urls import path
from .views import (
    show_all_data, 
    company_view, 
    employee_view, 
    device_view, 
    devicelog_view,
    devicelogreturn_view
)

urlpatterns = [
    path('all_data/', show_all_data, name='all_data'),
    path('company/', company_view, name='company'),
    path('employee/', employee_view, name='employee'),
    path('device/', device_view, name='device'),
    path('devicelog/', devicelog_view, name='devicelog'),
    path('devicelogreturn/', devicelogreturn_view, name='devicelogreturn'),
]
