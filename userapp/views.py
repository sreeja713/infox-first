# from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .models import student,course
from django.db import connection

from userapp.models import course
# Create your views here.


def home(request):
    return render(request, 'home.html')
 
def signup(request):
    return render(request,'signup.html')
def loginpage(request):
    return render(request,'login.html')
# @login_required(login_url='custom_login')
# def about(request):
#     # if request.user.is_authenticated:
#     return render(request,'about.html')
#     # return redirect(loginpage)
    

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username Already Exists!!')
                return redirect(signup)
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email
                )
                user.save()
                print("success")
        else:
            messages.info(request,'Password Doesnt match')
            print("Password Doesnt match")
            return redirect('signup')
        return redirect("loginpage")
    else:
        return render(request,'signup.html')
def custom_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password) 
        # request.session['uid']=user.id  #user id save to uid variable
        if user is not None:
            login(request,user)
            # auth.login(request,user)
            # request.session['uid']=user.id
            messages.info(request,f'Welcome {username}')
            return redirect ('add_course')
        else:
            messages.info(request,'invalid username or password')
            return redirect('loginpage')
    else:
        return redirect('loginpage')

@login_required(login_url='custom_login')
def logoutfunc(request):
    # if request.user.is_authenticated:
    # auth.logout(request)
    logout(request)
    print("\n logout\n")
    return redirect("home")

@login_required(login_url='custom_login')
def add_course(request):
    if request.method=="GET":
        return render(request,'course.html')
    else:
        cors=request.POST['course']
        cfee=request.POST['Cfee']
        print(cors)
        crs=course()
        crs.course_name=cors
        crs.fee=cfee
        crs.save()
        print("\nhiiiiii\n")
        return redirect('student1')

@login_required(login_url='custom_login')
def student1(request):
    courses=course.objects.all()
    context={'courses':courses}
    return render(request,'student.html',context)

def add_student(request):
    sname=request.POST['sname']
    address=request.POST['address']
    age=request.POST['age']
    jdate=request.POST['jdate']
    sel1=request.POST['sel']
    course1=course.objects.get(id=sel1)
    std=student(std_name=sname,std_address=address,std_age=age,join_date=jdate,course=course1)
    std.save()
    print("hiii")
    return redirect('show_details')

@login_required(login_url='custom_login')
def show_details(request):
    a1=student.objects.select_related('course')
    # for k in a1:
    #     print(k.course.__dict__)
    # # print("\n a1 is ",a1)
    # print(a1.query)
    # cursor = connection.cursor()
    # a1=cursor.execute("SELECT std_name,course_name  FROM userapp_course FULL JOIN userapp_student ON userapp_course.name=userapp_student.course_id")

    return render(request,'show_details.html',{'a1':a1})
    # stud=student.objects.all()

# @login_required(login_url='custom_login')
# def showone(request):
#     username_data=request.POST['username']
#     print(username_data)
#     curent_user=request.user
#     if curent_user==username_data:
#         a2=student.objects.get(curent_user=student.sname).select_related('course')
#         return render(request,'show_one.html',{'a2':a2})
    