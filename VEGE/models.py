from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null = True , blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    receipe_view_count=models.IntegerField(default =1)    #for number of receipes

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department

    # Indent this so it is INSIDE the Department class
    class Meta:
        ordering = ['department']
    


class studentID(models.Model):
    student_id= models.CharField(max_length=100) 

    def __str__(self) -> str:
        return self.student_id

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id= models.OneToOneField(studentID, related_name="studentid_relation", on_delete=models.CASCADE)
    student_name= models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default =18)
    student_address=models.TextField()

    def __str__(self) -> str:
        return self.student_name

        

    class Meta:
        ordering = ['student_name']  #order in ascending ig
        verbose_name = "student"

class StudentMarks(models.Model):
    student = models.ForeignKey(Student , related_name="studentmarks" , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)

    
    def __str__(self)->str:
        return f'{self.student.student_name} - {self.subject.subject_name}'

    class meta:
        unique_method =['student','subject'] #the combination of student and subject should be unique
        #a student should have only one entry per subject 
