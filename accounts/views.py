from django.shortcuts import render

# Create your views here.
def signup(request):
    
    return render(request, 'registration/signup.html')
def login(request):
    
    return render(request, 'registration/login.html')
def profile(request):
    
    return render(request, 'accounts/profile.html')


def profile_edit(request):
    
    return render(request, 'accounts/profile_edit.html')
