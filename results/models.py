# users/models.py
from django.db import models
from cusers.models import CustomUser
from django.utils import timezone
from django.urls import reverse
from django.conf import settings


class Subjects(models.Model):
    name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name 

class Grades(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Examination_Types(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Examination_Year(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

""" 
class StudentInformation(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(Subjects, max_length=200)
     """

""" 

class Sittings(models.Model):
    numberofsittings = models.IntegerField()
    studentinformation = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
 """
class ExaminationInfomation(models.Model):
    user = models.IntegerField(null = True)
    examtype = models.CharField(max_length=30)
    exam_number = models.CharField(max_length=30)
    exam_year = models.CharField(max_length=30)  

    @classmethod
    def create(cls, examtype, exam_number, exam_year, user):
        examinfo = cls(examtype=examtype, exam_number= exam_number,
        exam_year=exam_year, user=user)
        # do something with the book
        return examinfo

class StudentOlevels(models.Model):    
    #studentinformation = models.ForeignKey(StudentInformation, on_delete=models.CASCADE)
    user = models.IntegerField(null=True)
    subjects = models.IntegerField(null = True) #models.ForeignKey(Subjects, on_delete=models.CASCADE)
    grades = models.IntegerField(null = True) #models.ForeignKey(Grades, on_delete=models.CASCADE)
        
    @classmethod
    def create(cls, grades, subjects, user):
        studentolevel = cls(grades= grades, subjects=subjects, user=user)
        # do something with the book
        return studentolevel
    
    def save(self, *args, **kwargs):
        #self.isApplicationCreated = True
        super().save(*args, **kwargs)


