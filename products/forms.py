from django import forms
from django.forms import ModelForm, Form
from .models import Products


# Create the Class Form
class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['pd_name', 'pd_description', 'pd_price', 'pd_photo']


class NewUserForm(Form):
    login = forms.CharField(max_length=6)
    passwd = forms.CharField(max_length=6, widget=forms.PasswordInput)
