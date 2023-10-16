from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserAddress,UserHospitalManagement

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.CharField(max_length=10,choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    # //add extra characteristics in class
    
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','email','user_type','birth_date','gender','postal_code','city','street_address','country']
        
    def save(self,commit=True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            user_type = self.cleaned_data.get('user_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            
            UserAddress.objects.create(
                user=our_user,
                postal_code=postal_code,
                city=city,
                country=country,
                street_address=street_address
            )
            
            UserHospitalManagement.objects.create(
              user=our_user,
              user_type=user_type,
              gender=gender,
              birth_date=birth_date,
              employee_id = our_user.id
            )
        return our_user