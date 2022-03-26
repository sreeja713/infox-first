from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import Userform
from django.contrib.auth import authenticate, login , logout
from .models import student

# Create your views here.
def home(request):
    return render(request, 'home.html')

def update_user_data(user):
    student.objects.update_or_create(user=user, defaults={'std_address': student.std_address,'std_age': student.std_age,})
def signup(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  

            user.student.std_address = form.cleaned_data.get('std_address')
            user.student.std_age = form.cleaned_data.get('std_age')
            update_user_data(user)  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
 
            # redirect user to home page
            return redirect('home')
    else:
        form = Userform()
    return render(request, 'signup.html', {'form': form})
