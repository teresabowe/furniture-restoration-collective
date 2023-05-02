from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from . forms import ProductQuoteForm, ViewProductForm, ProductReviewForm
from django.http import JsonResponse
from django.template import loader
from django.http import HttpResponse


from .models import Product, Category, Crafter, Source, Subcategory, Review
from .forms import ProductForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().filter(quote="N")

    query = None
    categories = None
    crafters = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'crafter':
                sortkey = 'crafter__first_name'
            if sortkey == 'source':
                sortkey = 'source__source_name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'crafter' in request.GET:
            crafters = request.GET['crafter'].split(',')
            products = products.filter(crafter__first_name__in=crafters)
            crafters = Crafter.objects.filter(first_name__in=crafters)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) |\
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_crafters': crafters,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def list_products(request):
    """ List """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    else:
        listdata = Product.objects.all().values()
        template = loader.get_template('products/list_products.html')
        context = {
            'mylist': listdata,
        }

        return HttpResponse(template.render(context, request))


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('list_products'))
        else:
            messages.error(request, 'Product not added. Form must be valid.')
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('list_products'))
        else:
            messages.error(request, 'Product not updated. Form must be valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('list_products'))


@login_required
def view_product(request, product_id):
    """ View a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only shop owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    form = ViewProductForm(instance=product)
    form.fields['sku'].disabled = True
    form.fields['name'].disabled = True
    form.fields['description'].disabled = True
    form.fields['subcategory'].disabled = True
    form.fields['category'].disabled = True
    form.fields['quote'].disabled = True
    form.fields['price'].disabled = True
    form.fields['image'].disabled = True
    form.fields['crafter'].disabled = True
    form.fields['source'].disabled = True
    messages.info(request, f'You are viewing {product.name}')
    template = 'products/view_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def review_products(request):
    form = ProductReviewForm()
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProductReviewForm()

    return render(request, "products/product_review_form.html", {'form': form})


class ProductQuoteCreateView(CreateView):
    model = Product
    queryset = Product.objects.all().filter(quote="Y")
    form_class = ProductQuoteForm
    success_url = 'product_detail'
    template_name = 'products/quote_form.html'


# AJAX

def load_subcategories(request):
    category_id = request.GET.get('name')
    subcategories = Product.objects.filter(category_id=category_id) &\
        Product.objects.filter(quote="Y")
    print(subcategories)
    return render(request,
                  'products/subcategory_detail_dropdown_list_options.html',
                  {'subcategories': subcategories})


def load_price(request):
    subcategory_id = request.GET.get('name')
    price = Product.objects.filter(id=subcategory_id).first().price
    name = Product.objects.filter(id=subcategory_id).first().name
    id = Product.objects.filter(id=subcategory_id).first().id
    data = {'price': price, 'name': name, 'id': id}
    return JsonResponse(data)
