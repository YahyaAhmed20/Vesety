from django.contrib import admin

from .models import Specialty, Doctor, FeaturedCandidate

admin.site.register(Specialty)
admin.site.register(Doctor)
admin.site.register(FeaturedCandidate)

