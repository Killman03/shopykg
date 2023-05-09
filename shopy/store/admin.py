from django.contrib import admin

from .models import Category
from .models import Under_category
from .models import Articles

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'slug']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}

class UndercategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'slug', 'category_image']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'original_price', 'selling_price', 'is_published']
    list_filter = ['is_published']
    search_fields = ['title', 'specification']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Under_category, UndercategoryAdmin)
admin.site.register(Articles, ProductsAdmin)





# Register your models here.
