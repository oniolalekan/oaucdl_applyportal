# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from PIL import Image


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Local_Government_Area(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name  

class Programme_Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.name

class Programme_Session(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
     
    othernames = models.CharField('Other Names', max_length=50, null=True, blank=True)
    phone = models.CharField('Phone Number', max_length=20)
    birth_date = models.DateField('Date of Birth') 
    date_posted = models.DateTimeField(default=timezone.now)    
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    isApplicationCreated = models.BooleanField(default=True)
    isApplicationSubmitted = models.BooleanField(default=False)
    programme_course = models.ForeignKey(Programme_Course, on_delete=models.SET_NULL, null=True)
    programme_session = models.ForeignKey(Programme_Session, default= 2, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    local_government_area = models.ForeignKey(Local_Government_Area, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.email

    @property
    def userapplicationNumber(self):
         return "OAUCDL" + "%s%s%0.6d" % (self.programme_session.description, self.programme_course.description, self.user.id)


    
    def save(self, *args, **kwargs):
        #self.isApplicationCreated = True
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    programme_Course = models.ForeignKey(Programme_Course, default=6, on_delete=models.CASCADE)  #models.ForeignKey(State, on_delete=models.CASCADE)
    academic_session = models.ForeignKey(Programme_Session, default=2, on_delete=models.SET_NULL, null=True) #models.ForeignKey(Local_Government_Area, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    @property
    def applicationNumber(self):
         return "OAUCDL" + "%s%s%0.6d" % (self.academic_session.description, self.programme_Course.description, self.user.id)

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

   