from django.db import models
from django.urls import reverse
from django.utils import timezone
from patients.models import Patient
from staff.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('S', 'Scheduled'),
        ('C', 'Completed'),
        ('X', 'Cancelled'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='S')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"Appt for {self.patient} with {self.doctor} on {self.date} {self.time}"

    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])
