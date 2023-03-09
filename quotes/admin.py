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
    )


class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'quotecategory',
        'quotecategorydetail',
    )


admin.site.register(QuoteCategory, QuoteCategoryAdmin)
admin.site.register(QuoteCategoryDetail, QuoteCategoryDetailAdmin)
admin.site.register(Quote, QuoteAdmin)
