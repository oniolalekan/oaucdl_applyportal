from django import forms
from django.db import models
import datetime
from .models import Subjects, Grades, Examination_Types, Examination_Year


class ResultForm(forms.Form):

    exam_number = forms.CharField(label='', max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Exam Number'})
    )
   
    #exam_number = forms.CharField(max_length=25)
    exam_year = forms.ModelChoiceField(label='',empty_label="Exam Year", queryset=None)
    examination_type = forms.ModelChoiceField(label='',empty_label="Exam Type", queryset=None)
    subject_one = forms.ModelChoiceField(label='', empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_one = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_two = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_two = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_three = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_three = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_four = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_four = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_five = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_five = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_six = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_six = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_seven = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_seven = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_eight = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_eight = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())
    subject_nine = forms.ModelChoiceField(label='',empty_label="Select Subject", queryset=Subjects.objects.all())
    grade_nine = forms.ModelChoiceField(label='', empty_label="Grade", queryset=Grades.objects.all())


    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields['examination_type'].queryset = Examination_Types.objects.all()
        self.fields['exam_year'].queryset = Examination_Year.objects.all()   
       
        #super().__init__(*args, **kwargs)

        self.fields['subject_two'].required = False 
        self.fields['grade_two'].required = False 
        self.fields['subject_three'].required = False 
        self.fields['grade_three'].required = False 
        self.fields['subject_four'].required = False 
        self.fields['grade_four'].required = False
        self.fields['subject_five'].required = False 
        self.fields['grade_five'].required = False


        self.fields['subject_six'].required = False 
        self.fields['grade_six'].required = False 
        self.fields['subject_seven'].required = False 
        self.fields['grade_seven'].required = False 
        self.fields['subject_eight'].required = False 
        self.fields['grade_eight'].required = False
        self.fields['subject_nine'].required = False 
        self.fields['grade_nine'].required = False

    