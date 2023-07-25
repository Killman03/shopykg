from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'slug']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'original_price', 'selling_price', 'is_published', 'slug', 'is_trending', 'is_new',
                    'is_best', 'category', 'image']
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'specification']
    list_editable = ['is_published', 'category', 'image']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)





# Register your models here.
