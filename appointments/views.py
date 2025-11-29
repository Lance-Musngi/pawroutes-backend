from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by("appointment_date", "appointment_time")
    serializer_class = AppointmentSerializer
