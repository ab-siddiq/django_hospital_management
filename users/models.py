from django.db import models
from django.contrib.auth.models import User
from .constants import USER_TYPE,GENDER_TYPE
# Create your models here.

class UserHospitalManagement(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    user_type = models.CharField(max_length=30,choices=USER_TYPE)
    employee_id = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.employee_id)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.email