from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import StripeCustomer
from django.contrib.auth.models import User
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, user):
        """Send the user a confirmation email"""
        cust_email = user.email
        subject = render_to_string(
            'membership/confirmation_emails/confirmation_email_subject.txt',
            {'StripeCustomer': StripeCustomer})
        body = render_to_string(
            'membership/confirmation_emails/confirmation_email_body.txt',
            {'StripeCustomer': StripeCustomer, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_checkout_session_completed(self, event):
        """
        Handle the checkout.session.completed webhook from Stripe
        """

        intent = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = intent.get('client_reference_id')
        stripe_customer_id = intent.get('customer')
        stripe_subscription_id = intent.get('subscription')
        print(client_reference_id)
        print(stripe_customer_id)
        print(stripe_subscription_id)

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )

        profile = get_object_or_404(UserProfile, user=user)
        profile.membership = 'active'
        profile.save()

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_customer_subscription_deleted(self, event):

        event_object = event['data']['object']

        customer = stripe.Customer(event_object['customer'])

        user = get_object_or_404(StripeCustomer, stripeCustomerId=customer['id'])
        # user.delete()

        profile = get_object_or_404(UserProfile, user=user['user'])
        # profile.membership = 'deleted'
        # profile.save()

        print(user)
        print(profile)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
