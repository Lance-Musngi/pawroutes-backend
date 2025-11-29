from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appointments.urls')),  # Your appointments API
    path('', views.home_api, name='home_api'),   # Root API endpoint
]
