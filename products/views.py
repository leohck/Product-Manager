from django.shortcuts import render
from .models import Products

# Create your views here.
def home(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user.html')


def products(request):
    produtos = Products.objects.all()
    context = {'produtos': produtos}
    return render(request, 'products.html', context=context)
