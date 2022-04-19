from django.db import models
from django.contrib.auth.models import User
from django.core.files import File
import os
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank = True)    
    name = models.CharField(max_length=200, null = True)

    def __str__(self):
         return self.name




class Product(models.Model):
    name = models.CharField(max_length= 150)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    store = models.CharField(max_length=30)
    category = models.CharField(max_length=150)
    image = models.ImageField(null = True, blank = True)
    image_url = models.URLField()
    

   

    def __str__(self):
        return self.name

    #Prevent error when no image is present for product
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def clean(self, *args, **kwargs):
        if self.image_url and not self.image:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.image_url).read())
            img_temp.flush()
            self.image.save(f"image_{self.pk}.jpg", File(img_temp))
        super(Product, self).save(*args, **kwargs)

    @property
    def product_by_id(self):
        return Product.objects.get(pk=self.id)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null= True, blank= True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null = True)
    quantity = models.IntegerField(default=0, null = True, blank = True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
