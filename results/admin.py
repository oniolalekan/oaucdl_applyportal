from django.contrib import admin

from .models import ExaminationInfomation, Examination_Year, Examination_Types, Grades, StudentOlevels, Subjects

# Register your models here.

admin.site.register(Examination_Types)

admin.site.register(Examination_Year)

admin.site.register(ExaminationInfomation)

admin.site.register(Grades)

admin.site.register(StudentOlevels)

admin.site.register(Subjects)


