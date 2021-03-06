from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de telefono debe tener el siguiente: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, unique=True, verbose_name="Telefono") # validators should be a list
    email = models.EmailField(max_length=200, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    #def __str__(self):
    #    return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
        

class Order(models.Model):
    
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
