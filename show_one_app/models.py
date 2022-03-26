from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
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
    std_address=models.CharField(max_length=255)
    std_age=models.IntegerField(blank=True,null=True)
    join_date=models.DateField(blank=True,null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        student.objects.create(UID=instance)
    instance.student.save()