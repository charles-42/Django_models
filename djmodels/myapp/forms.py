from django import forms
from myapp.models import User

class UserForm(forms.ModelForm):
   class Meta:
     model = User
     fields = '__all__'

class NameForm(forms.Form):
    your_name = forms.CharField(label='Votre nom', max_length=100, required=False)
