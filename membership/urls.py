from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('config/', views.stripe_config),

]
