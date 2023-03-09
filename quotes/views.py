from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Quote, QuoteCategoryDetail
from . forms import QuoteForm
from django.shortcuts import render


class QuoteListView(ListView):
    model = Quote
    context_object_name = 'quotes'


class QuoteCreateView(CreateView):
    model = Quote
    form_class = QuoteForm
    success_url = '/quotes/add/'


class QuoteUpdateView(UpdateView):
    model = Quote
    form_class = QuoteForm
    success_url = '/quotes/add/'


# AJAX
def load_categories(request):
    quotecategory_id = request.GET.get('quotecategory')
    category_detail = QuoteCategoryDetail.objects.filter(quotecategory_id=quotecategory_id).all()
    return render(request, 'quotes/category_detail_dropdown_list_options.html', {'category_detail': category_detail})
