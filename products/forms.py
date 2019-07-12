from django.forms import ModelForm
from .models import Products


# Create the Class Form
class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['pd_name', 'pd_description', 'pd_price', 'pd_photo']
