from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),

    path('quote/', views.ProductQuoteCreateView.as_view(), name='product_quote_add'),

    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('ajax/load-price/', views.load_price, name='ajax_load_price'),
]
