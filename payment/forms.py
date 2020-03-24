# users/forms.py
from django import forms
from .models import Invoice


class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = Invoice
        fields = ['last_name', 'first_name' , 'email', 
        'narration', 'amount']
