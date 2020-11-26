from django.db import models

# Create your models here.
# Create your models here.
class major(models.Model):
    subj_name=models.CharField(max_length=30)
    teacher_name=models.CharField(max_length=20)
class course(models.Model):
    course_id=models.CharField(max_length=20)
    dur=models.IntegerField
    subj=models.ForeignKey(major,on_delete=models.SET_NULL,null=True)


class student(models.Model):

    roll=models.IntegerField(primary_key=True)
    sname=models.TextField(max_length=30 ,null=True)
    dob=models.DateField()
    course_id=models.ForeignKey(course,on_delete=models.SET_NULL,null=True)

class teacher(models.Model)
    teacher_name=models.CharField(max_length=True)