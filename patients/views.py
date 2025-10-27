from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            p = form.save()
            return redirect(p.get_absolute_url())
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form})
