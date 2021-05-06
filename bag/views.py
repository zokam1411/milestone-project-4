from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contants page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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
            else:
                bag[item_id]['items_by_turns'][turns] = quantity
        else:
            bag[item_id] = {'items_by_turns': {turns: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    turns = None
    if 'product_turns' in request.POST:
        turns = request.POST['product_turns']
    bag = request.session.get('bag', {})

    if turns:
        if quantity > 0:
            bag[item_id]['items_by_turns'][turns] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
