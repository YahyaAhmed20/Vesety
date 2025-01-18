# models.py
from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    waiting_time = models.IntegerField(help_text="Waiting time in hours")
    working_hours = models.IntegerField(help_text="Working hours per day")
    phone_number = models.CharField(max_length=15)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class FeaturedCandidate(models.Model):
        
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='featured_candidates/', null=True, blank=True)
    def __str__(self):
        return self.doctor.name