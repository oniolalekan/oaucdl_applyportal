from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ApplyCreateView
)
from . import views

urlpatterns = [
    
    path('', ApplyCreateView.as_view(), name='apply-create'),
    path('about/', views.about, name='blog-about'),
]
