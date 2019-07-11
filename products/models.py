from django.db import models


# Create your models here.
class Products(models.Model):
    pd_name = models.CharField(max_length=30)
    pd_description = models.TextField()
    pd_price = models.DecimalField(max_digits=6, decimal_places=2)
    pd_photo = models.ImageField(upload_to='products_photos', null=True, blank=True)

    def __str__(self):
        return self.pd_name
