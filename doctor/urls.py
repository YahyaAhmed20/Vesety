# blog


from django.urls import path

from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.add_new_doctor, name='doctor'),
    path('delete_doctor', views.delete_doctor, name='doctor'),
    path('update_doctor', views.update_doctor, name='doctor'),
]

