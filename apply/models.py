from django.db import models
from django.utils import timezone 
# from django.contrib.auth.models import User
from cusers.models import CustomUser
from django.urls import reverse
from django.conf import settings

class Apply(models.Model):
    DEFAULT = -1
    APPRECIATION = 'AP'
    PYTHONDJANGO = 'PD'
    MAINTENANCE = 'MT'
    CERTIFICATE_COURSE_CHOICES = (
        (DEFAULT, '--Select Programme--'),
        (APPRECIATION, 'Computer Appreciation'),
        (PYTHONDJANGO, 'Python with Django'),
        (MAINTENANCE, 'Computer Maintenance'),
    )
    
    surname = models.CharField('Surname', max_length=50)
    firstname = models.CharField('First Name', max_length=50)
    othernames = models.CharField('Other Names', max_length=50)
    phone = models.CharField('Phone Number', max_length=20)
    birth_date = models.DateField('Date of Birth') #input_formats = settings.DATE_INPUT_FORMATS
    isApplicationSubmitted = models.BooleanField(default=False)
    courses_in_programme = models.CharField(max_length=2,
                                      choices=CERTIFICATE_COURSE_CHOICES,
                                      default=DEFAULT)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.OneToOneField(CustomUser, on_delete=models.CASCADE) #use one-to-one relationship here: change it to 

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('payment-home')
