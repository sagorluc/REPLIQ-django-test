
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('device/', include('Device.urls')),
    path('api/', include('API.urls')),
]
