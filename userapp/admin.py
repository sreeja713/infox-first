from django.contrib import admin

# Register your models here.
from .models import course,student

@admin.register(course)
class course_admin(admin.ModelAdmin):
    list_display=('course_name','fee')

@admin.register(student)
class student_admin(admin.ModelAdmin):
    list_display=('course','std_name','std_address','std_age','join_date')