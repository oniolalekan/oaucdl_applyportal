from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('load-locals/', views.load_locals, name='load_locals'),
]
