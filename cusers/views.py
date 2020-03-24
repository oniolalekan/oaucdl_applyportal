from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm
from .models import Local_Government_Area
# from biodata.models import PersonalInfo


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cusers/register.html', {'form': form})


@login_required
def userprofile(request):
    if (request.method == 'POST') and (request.user.isApplicationSubmitted == False):
        u_form = CustomUserChangeForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    elif request.user.isApplicationSubmitted == False:
        u_form = CustomUserChangeForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
     

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'cusers/profile.html', context)
    else: 
        return redirect('results-home')


def load_locals(request):
    state_id = request.GET.get('state')
    locals = Local_Government_Area.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'cusers/locals_dropdown_list_options.html', {'locals': locals})