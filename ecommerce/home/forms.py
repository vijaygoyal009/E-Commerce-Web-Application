from django import forms
class registation_form(forms.Form):
    First_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    Email=forms.EmailField()
    password=forms.CharField(max_length=40)