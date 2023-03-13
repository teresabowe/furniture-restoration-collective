from django.contrib import admin
from .models import QuoteCategory, QuoteCategoryDetail, Quote


class QuoteCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class QuoteCategoryDetailAdmin(admin.ModelAdmin):
    list_display = (
        'quotecategory',
        'name',
        'price',
    )


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'quotecategory',
        'quotecategorydetail',
        'pickup',
        'base_price',
        'pickup_price',
        'total_price',
        'date',
    )


admin.site.register(QuoteCategory, QuoteCategoryAdmin)
admin.site.register(QuoteCategoryDetail, QuoteCategoryDetailAdmin)
admin.site.register(Quote, QuoteAdmin)
