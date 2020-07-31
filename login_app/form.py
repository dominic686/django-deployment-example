from django import forms

from django.contrib.auth.models import User
from login_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    confirm_password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password confirmation does not match")

class UserProfileInfo(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
