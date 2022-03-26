
from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
    
    def __str__(self):
        return self.course_name

class student(models.Model):
    UID=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    std_name=models.CharField(max_length=255)
    std_address=models.CharField(max_length=255)
    std_age=models.IntegerField()
    join_date=models.DateField()