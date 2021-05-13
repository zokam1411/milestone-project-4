from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    membership = None

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for turns, quantity in item_data['items_by_turns'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'turns': turns,
                })

    if membership == 'Member':
        discount = total * Decimal(settings.MEMBER_DISCOUNT / 100)
        delivery = total * Decimal(settings.MEMBER_DISCOUNT / 100)
    else:
        discount = total * Decimal(settings.GUEST_DISCOUNT / 100)
        delivery = total * Decimal(settings.GUEST_DELIVERY / 100)


    grand_total = total - discount + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
