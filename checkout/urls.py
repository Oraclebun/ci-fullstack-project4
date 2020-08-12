from django.urls import path
from .views import checkout, checkout_success, checkout_cancel

urlpatterns = [
    path('', checkout, name='checkout'),
    path('success', checkout_success,
         name="checkout_success"),
    path('cancelled', checkout_cancel,
         name="checkout_cancelled"),
]