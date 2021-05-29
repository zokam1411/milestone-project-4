from django.contrib import admin
from membership.models import StripeCustomer

class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'stripeCustomerId',
        'stripeSubscriptionId',
    )

admin.site.register(StripeCustomer, StripeCustomerAdmin)
