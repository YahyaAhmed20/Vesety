from django.shortcuts import render



def add_new_doctor(request):
    
    return render(request,'doctor/add_new_doctor.html')
    
    
def delete_doctor(request):
    return render(request,'doctor/delete_doctor.html')
    
    
def update_doctor(request):
    return render(request,'doctor/update_doctor.html')