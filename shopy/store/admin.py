from django.contrib import admin

from .models import Category
from .models import Products

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'slug']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'original_price', 'selling_price', 'is_published', 'slug', 'is_trending', 'is_new',
                    'is_best', 'category', 'image']
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'specification']
    list_editable = ['is_published', 'category', 'image']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)





# Register your models here.
