from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import ResultForm
from .models import ExaminationInfomation, StudentOlevels

@login_required
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = ResultForm(request.POST)

        #create examinationinformation object
        examinfo = ExaminationInfomation.create(request.POST['examination_type'], request.POST['exam_number'], request.POST['exam_year'], request.user.id)

        studentolevel_list = []
        studentolevel_1 = StudentOlevels.create(request.POST['grade_one'], request.POST['subject_one'], request.user.id)
        studentolevel_list.append(studentolevel_1)

        studentolevel_2 = StudentOlevels.create(request.POST['grade_two'], request.POST['subject_two'], request.user.id)
        studentolevel_list.append(studentolevel_2)

        studentolevel_3 = StudentOlevels.create(request.POST['grade_three'], request.POST['subject_three'], request.user.id)
        studentolevel_list.append(studentolevel_3)

        studentolevel_4 = StudentOlevels.create(request.POST['grade_four'], request.POST['subject_four'], request.user.id)
        studentolevel_list.append(studentolevel_4)

        studentolevel_5 = StudentOlevels.create(request.POST['grade_five'], request.POST['subject_five'], request.user.id)
        studentolevel_list.append(studentolevel_5)

        studentolevel_6 = StudentOlevels.create(request.POST['grade_six'], request.POST['subject_six'], request.user.id)
        studentolevel_list.append(studentolevel_6)

        studentolevel_7 = StudentOlevels.create(request.POST['grade_seven'], request.POST['subject_seven'], request.user.id)
        studentolevel_list.append(studentolevel_7)

        studentolevel_8 = StudentOlevels.create(request.POST['grade_eight'], request.POST['subject_eight'], request.user.id)
        studentolevel_list.append(studentolevel_8)

        studentolevel_9 = StudentOlevels.create(request.POST['grade_nine'], request.POST['subject_nine'], request.user.id)
        studentolevel_list.append(studentolevel_9)
        #create list of studentolevel obeject

        # creating list        
        #  
  
        # appending instances to list  
        
        print(request.POST['grade_one'])
        print(request.POST['subject_one'])
        #list.append( StudentOlevels('Akash', 2) ) 
        
        # check whether it's valid:
        if form.is_valid():
            print("not here")
            for item in studentolevel_list:
                item.save()
            examinfo.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('results-home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResultForm()

    return render(request, 'results/home.html', {'form': form})

""" 
@login_required
def home(request):    

    #p_form = ProfileFieldForm(instance=request.user.userprofile)
    r_form = ResultForm(instance=request.user)       
    
    context = {
        
        'r_form': r_form
    }

    return render(request, 'results/home.html', context)

 """
