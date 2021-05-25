from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.membership, name='membership'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('wh/', webhook, name='webhook'),
]
