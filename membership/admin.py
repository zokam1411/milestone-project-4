from django.contrib import admin
from membership.models import StripeCustomer


admin.site.register(StripeCustomer)
