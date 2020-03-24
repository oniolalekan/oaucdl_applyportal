# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile, Local_Government_Area


class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name', 'othernames', 
        'email', 'phone', 'birth_date', 'programme_session', 'state', 'local_government_area']
        widgets = {
            'birth_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):        
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = True
        self.fields['first_name'].required = True
        self.fields['local_government_area'].queryset = Local_Government_Area.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['local_government_area'].queryset = Local_Government_Area.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['local_government_area'].queryset = self.instance.state.local_government_area_set.order_by('name')     

class CustomUserChangeForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'last_name', 'first_name' , 'othernames', 
        'email', 'phone', 'birth_date', 'programme_course', 'programme_session']
        widgets = {
            'birth_date': DateInput(),
        }

   


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
