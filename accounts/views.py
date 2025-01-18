from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the home page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
def profile(request):
    
    return render(request, 'accounts/profile.html')


def profile_edit(request):
    
    return render(request, 'accounts/profile_edit.html')
