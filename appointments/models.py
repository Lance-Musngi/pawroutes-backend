from django.db import models

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ("Bath", "Bath"),
        ("Haircut", "Haircut"),
        ("Nail Trim", "Nail Trim"),
        ("Full Grooming", "Full Grooming"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    pet_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet_name} - {self.service_type} on {self.appointment_date}"
