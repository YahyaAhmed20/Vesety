# home


from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/<int:doctor_id>/', views.doctor_list, name='doctor_list'),  # Ensure this line exists
    
   

    
]