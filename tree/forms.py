from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=12)
    password = forms.CharField(max_length=10)
    