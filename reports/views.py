from django.shortcuts import render, get_object_or_404
import requests
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from payment.models import Receipts
from cusers.models import CustomUser
from django.contrib import messages

# Create your views here.


@login_required
def home(request):

    payReference = request.GET.get('paymentReference')
    processId = request.GET.get('processorId')
    transactId = request.GET.get('transactionId')
    message = request.GET.get('message')
    amt = request.GET.get('amount')  
    
    p = Receipts.create(request.user.id, payReference, processId, transactId,message,amt)
    p.save()
    cuser = get_object_or_404(CustomUser, pk=request.user.id)
    cuser.isApplicationSubmitted = True
    cuser.save()
    messages.success(request, f'Payment Successful for {request.user.email}!')    
    return render(request, 'reports/home.html')


