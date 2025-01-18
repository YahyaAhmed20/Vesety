# views.py
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Doctor, Specialty,FeaturedCandidate
def home(request):
    doctors = Doctor.objects.all()
    specialties = Specialty.objects.all()
    featured_candidates = FeaturedCandidate.objects.all()

    query = request.GET.get('q')
    location = request.GET.get('location')
    specialty = request.GET.get('specialty')
    
    if query:
        doctors = doctors.filter(Q(name__icontains=query))
    if location:
        doctors = doctors.filter(location__icontains=location)
    if specialty:
        doctors = doctors.filter(specialty__name__icontains=specialty)
        
    context = {
        'doctors': doctors,
        'specialties': specialties,
        'featured_candidates': featured_candidates,

    }
    
  
    return render(request, 'home/home.html',context)

def doctor_list(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'home/doctor_list.html', {'doctor': doctor})