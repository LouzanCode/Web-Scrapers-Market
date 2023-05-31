from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('tienda:category_list', args=[self.slug])

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    requirements = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    code = models.FileField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('tienda:product_detail', args=[self.slug])
    
    def __str__(self):
        return self.title