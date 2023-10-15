from django.contrib import admin
from .models import UserAddress,UserHospitalManagement
# Register your models here.
admin.site.register(UserHospitalManagement)
admin.site.register(UserAddress)
