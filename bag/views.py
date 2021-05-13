from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contants page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    turns = None
    if 'product_turns' in request.POST:
        turns = request.POST['product_turns']
    bag = request.session.get('bag', {})

    if turns:
        if item_id in list(bag.keys()):
            if turns in bag[item_id]['items_by_turns'].keys():
                bag[item_id]['items_by_turns'][turns] += quantity
                messages.success(
                    request, f'{product.name} - {turns.upper()} turns quantity updated to {bag[item_id]["items_by_turns"][turns]}')
            else:
                bag[item_id]['items_by_turns'][turns] = quantity
                messages.success(
                    request, f'{product.name} - {turns.upper()} turns added to bag')

        else:
            bag[item_id] = {'items_by_turns': {turns: quantity}}
            messages.success(
                request, f'{product.name} - {turns.upper()} turns added to bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'{product.name} quantity updated to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} added to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    turns = None
    if 'product_turns' in request.POST:
        turns = request.POST['product_turns']
    bag = request.session.get('bag', {})

    if turns:
        if quantity > 0:
            bag[item_id]['items_by_turns'][turns] = quantity
            messages.success(
                request, f'{product.name} - {turns.upper()} turns quantity updated to {bag[item_id]["items_by_turns"][turns]}')
        else:
            del bag[item_id]['items_by_turns'][turns]
            if not bag[item_id]['items_by_turns']:
                bag.pop(item_id)
            messages.success(
                request, f'{product.name} - {turns.upper()} turns removed from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'{product.name} quantity updated to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} removed from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        turns = None
        if 'product_turns' in request.POST:
            turns = request.POST['product_turns']
        bag = request.session.get('bag', {})

        if turns:
            del bag[item_id]['items_by_turns'][turns]
            if not bag[item_id]['items_by_turns']:
                bag.pop(item_id)
            messages.success(
                request, f'{product.name} - {turns.upper()} turns removed from bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} removed from bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
