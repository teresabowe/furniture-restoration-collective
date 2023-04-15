from django.shortcuts import render
from products.models import Review
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    Return the index page with reviews list
    """
    reviews_list = Review.objects.all().values()
    template = loader.get_template('home/index.html')
    context = {
            'reviews_list': reviews_list,
        }

    return HttpResponse(template.render(context, request))
