from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    path('', views.home, name='results-home'),
    #path('paid', views.home, name='report-paid'),
    #path('demo/', views.demo, name='payment-demo'),
    #path('checkout/', views.checkout, name='payment-checkout'),
    #path('invoice/', views.PaymentListView.as_view(), name='payment-invoice'),
]
