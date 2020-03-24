from django.shortcuts import render, get_object_or_404
import requests
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from cusers.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'payment/home.html')


@login_required
def checkout(request):
    return render(request, 'payment/checkout.html')


class PaymentListView(LoginRequiredMixin, ListView):

    model = CustomUser
    template_name = 'payment/invoice.html'
    #template_name = 'payment/customuser_list.html'
    context_object_name = 'payment'

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id).first()