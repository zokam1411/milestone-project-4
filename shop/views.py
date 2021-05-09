from django.shortcuts import render

from products.models import Product, Category

# Create your views here.

def shop(request):
    """ A view to return shop page """

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/shop.html', context)