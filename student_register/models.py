from django.db import models

# Create your models 

class Student(models.Model):
    Name = models.CharField(max_length=100,default= 0)
    Reg_no = models.CharField(max_length=50)
    Mobile_no = models.IntegerField(null=False)
    Student_email = models.EmailField(max_length=20)
    Intake_year = models.DateField(auto_now=False)

class Hostel(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE,default = True)
    Student_stay = models.BooleanField(default=False)
    Members_in_room = models.IntegerField(null=True)

    
    

 
    
    




 
    
    



