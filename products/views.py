from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from products.forms import ProductForm, NewUserForm
from .models import Products


# Create your views here.
def home(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user.html')


def newuser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user_login = cd.get('login')
            user_passwd = cd.get('passwd')
            new = User.objects.create_user(
                username=user_login,
                password=user_passwd,
            )
            new.save()
            return redirect('user')
    else:
        form = NewUserForm()
    context = {'NewUserForm': form}
    return render(request, 'newuser.html', context=context)


def products(request):
    produtos = Products.objects.all()
    context = {'products': produtos}
    return render(request, 'products.html', context=context)


@login_required
def product_new(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'ProductForm': form}
    return render(request, 'product_new.html', context=context)


@login_required
def product_update(request, id_product):
    product = get_object_or_404(Products, pk=id_product)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'ProductForm': form}
    return render(request, 'product_new.html', context=context)


@login_required
def product_delete(request, id_product):
    product = get_object_or_404(Products, pk=id_product)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'product': product}
    return render(request, 'product_delete_confirm.html', context=context)
