from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your vag at the moment")
        return redirect (reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IrLgtB0bW0Bx3RA2mB24QpNm8752ccGepScrDjpRail1PAiXIqiWTzMP0deJ837UgkOKb3oXTF31EUzLZTc9GKf00MyhQx1D3',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    