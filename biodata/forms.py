from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PersonalInfo, Local_Government_Area



class PersonalInfoRegisterForm(forms.ModelForm):
    #email = forms.EmailField()

    class Meta:
        model = PersonalInfo
        fields = [ 'courses_programme', 'state', 'local_government_area']

class PersonalInfoUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PersonalInfo
        fields = ['courses_programme', 'state', 'local_government_area']

class PersonForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ['courses_programme', 'state', 'local_government_area']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['local_government_area'].queryset = Local_Government_Area.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['local_government_area'].queryset = Local_Government_Area.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['local_government_area'].queryset = self.instance.state.local_government_area_set.order_by('name')

    


