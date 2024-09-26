from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Hostel

admin.site.register(Student)
admin.site.register(Hostel)
