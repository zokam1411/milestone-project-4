from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.contrib.auth.models import User
from membership.models import StripeCustomer
from profiles.models import UserProfile

import stripe

# Create your views here.


def membership(request):
    """ A view to display the memberships page """
    if request.user.is_authenticated:
        try:
            # Retrieve the subscription & product
            stripe_customer = StripeCustomer.objects.get(user=request.user)
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscription = stripe.Subscription.retrieve(
                stripe_customer.stripeSubscriptionId)
            product = stripe.Product.retrieve(subscription.plan.product)

            context = {
                'subscription': subscription,
                'product': product,
                'on_membership_page': True,
            }

            return render(request, 'membership/membership.html', context)

        except StripeCustomer.DoesNotExist:
            return render(request, 'membership/membership.html')

    else:
        return render(request, 'membership/membership.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLIC_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url +
                'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )

            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@login_required
def success(request):
    return render(request, 'membership/success.html')


@login_required
def cancel(request):
    return render(request, 'membership/cancel.html')
