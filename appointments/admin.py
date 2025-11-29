from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "pet_name", "owner_name", "service_type", "appointment_date", "appointment_time", "status")
    list_filter = ("service_type", "status")
    search_fields = ("pet_name", "owner_name")
