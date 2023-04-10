from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),

    path('quote/', views.ProductQuoteCreateView.as_view(), name='product_quote_add'),

    path('list/', views.list_products, name='list_products'),
    path('review/', views.review_products, name='review_products'),
    path('view/<int:product_id>/', views.view_product, name='view_product'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('ajax/load-price/', views.load_price, name='ajax_load_price'),
]
