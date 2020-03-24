from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PersonForm, PersonalInfoRegisterForm, PersonalInfoUpdateForm
from django.contrib.auth.models import User
from .models import PersonalInfo, Local_Government_Area
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class PersonListView(ListView):
    model = PersonalInfo
    context_object_name = 'people'

class PersonCreateView(LoginRequiredMixin, CreateView):
    model = PersonalInfo
    form_class = PersonForm
    #fields = ('surname', 'firstname', 'state', 'local_government_area')
    success_url = reverse_lazy('person_changelist')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)


class PersonUpdateView(UpdateView):
    model = PersonalInfo
    form_class = PersonForm    
    success_url = reverse_lazy('person_changelist')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    
def load_locals(request):
    state_id = request.GET.get('state')
    locals = Local_Government_Area.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'biodata/locals_dropdown_list_options.html', {'locals': locals})

""" @login_required
def biodata(request):
    if request.method == 'POST':
        form = PersonalInfoRegisterForm(request.POST)
        form.instance.user_id = request.user.id
        form.instance.isApplicationCreated = True
        if form.is_valid():
            form.save()
            surname = form.cleaned_data.get('surname')
            messages.success(request, f'Personal Information created successfully {surname}!')
            return redirect('payment-checkout')
    else:
        form = PersonalInfoRegisterForm()
    return render(request, 'biodata/personInfo.html', {'form': form}) """

"""
    Redirects users based on whether they have created application or not
    """
""" def login_success(request):
    
    person = PersonalInfo.objects.filter(user.id).first()
    if person is not None:
    
        return redirect("payment-checkout")
    else:
        return redirect("biodata") 
 """
