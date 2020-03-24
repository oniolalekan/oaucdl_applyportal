from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.home, name='payment-home'),
    #path('checkout/', views.checkout, name='payment-checkout'),
    path('invoice/', views.PaymentListView.as_view(), name='payment-invoice'),
]
