from django.contrib import admin

# Register your models here.
from .models import Sequence, Specimen

admin.site.register(Sequence)
admin.site.register(Specimen)