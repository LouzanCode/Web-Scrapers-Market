from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'created', 'updated']
    list_filter = ['is_active', ]
    list_editable = ['price', ]
    prepopulated_fields = {'slug': ('title',)}