from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.QuoteListView.as_view(), name='quote_changelist'),
    path('add/', views.QuoteCreateView.as_view(), name='quote_add'),
    path('<int:pk>/', views.QuoteUpdateView.as_view(), name='quote_change'),

    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
]
