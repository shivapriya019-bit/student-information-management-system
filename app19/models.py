from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be exactly 10 digits.'
)


# Create your models here.
class Student(models.Model):
    studentID=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    Age=models.IntegerField()
    gender= [
        ('male' ,'Male'),
        ('female','Female'),
    ]
    gender = models.CharField(max_length=10, choices=gender)
    Email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=10,validators=[phone_validator],
    unique=True)
    Address=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    DOJ=models.DateField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    
    def __str__(self):
        return f"{self.studentID} - {self.name} - {self.Age} - {self.Email} -{self.phonenumber} -{self.gender} - {self.Address} - {self.course} - {self.DOJ} - {self.profile_picture}"
     
