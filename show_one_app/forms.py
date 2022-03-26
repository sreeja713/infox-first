
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Userform(UserCreationForm):
    std_address=forms.CharField(max_length=255)
    std_age=forms.IntegerField()
    join_date=forms.DateField()
    class Meta:
        model = User
        fields = ('first_name','last_name','std_address','std_age','join_date','username','email', 'password1', 'password2' )
     
