from django.db import models
# from django.contrib.auth.models import User
from cusers.models import CustomUser
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
#from PIL import Image



class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Local_Government_Area(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name   

class Courses_Programme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class PersonalInfo(models.Model):    
        
    courses_programme = models.ForeignKey(Courses_Programme, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    local_government_area = models.ForeignKey(Local_Government_Area, on_delete=models.SET_NULL, null=True)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    """ def __str__(self):
        return f'{self.surname} Personal Information' """

    
    def sava(self, *args, **kwargs):
        super().save(*args, **kwargs)

        """ img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) """



