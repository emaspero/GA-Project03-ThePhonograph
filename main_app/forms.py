from django.forms import ModelForm
from .models import Tracklist, Artist
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




    

class TracklistForm(forms.ModelForm):

    class Meta:
        model = Tracklist
        fields = ['track_name', 'track_duration']

# New User Form here (this allows the user to input email, first and last name as well when signing up)
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user




