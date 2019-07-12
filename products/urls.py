from django.urls import path
from .views import home, products, product_delete, product_new, product_update


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('new/', product_new, name='product_new'),
    path('update/<int:id_product>/', product_update, name='product_update'),
    path('delete/<int:id_product>/', product_delete, name='product_delete'),
]
