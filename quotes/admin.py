from django.contrib import admin
from .models import QuoteCategory, QuoteCategoryDetail, Quote


class QuoteCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'quote_category_name',
        'quote_category_friendly_name',
    )


class QuoteCategoryDetailAdmin(admin.ModelAdmin):
    list_display = (
        'quote_category_detail_name',
        'quote_category_detail_friendly_name',
    )


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'quote_number',
        'quote_category_detail_name',
    )


admin.site.register(QuoteCategory, QuoteCategoryAdmin)
admin.site.register(QuoteCategoryDetail, QuoteCategoryDetailAdmin)
admin.site.register(Quote, QuoteAdmin)
