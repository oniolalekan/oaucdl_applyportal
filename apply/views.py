from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Apply


""" def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
 """
def home(request):
    return render(request, 'users/login.html')


class ApplyCreateView(LoginRequiredMixin, CreateView):
    model = Apply
    fields = ['surname', 'firstname', 'othernames', 'phone', 'birth_date', 'courses_in_programme']
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
