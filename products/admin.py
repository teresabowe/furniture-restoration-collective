from django.contrib import admin
from .models import Product, Category, Crafter, Source, Subcategory


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'subcategory',
        'quote',
        'price',
        'crafter',
        'source',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CrafterAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'full_name',
        'specialisation',
    )


class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'source_name',
        'source_friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Crafter, CrafterAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)

