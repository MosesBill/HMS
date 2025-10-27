from django.contrib import admin
from .models import Patient, MedicalRecord

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'national_id', 'phone', 'email', 'created_at')
    search_fields = ('first_name', 'last_name', 'national_id', 'phone')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'diagnosis', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'diagnosis')
