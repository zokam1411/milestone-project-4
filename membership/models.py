from django.contrib.auth.models import User
from django.db import models


class StripeCustomer(models.Model):

    class Meta:
        verbose_name_plural = 'Stripe Customers'

    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username
        