from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    #path('', views.biodata, name='biodata'),
    #path('', views.biodata, name='biodata'),
    path('', views.PersonCreateView.as_view(), name='person_changelist'),
    path('person/', views.PersonListView.as_view(), name='person_list'),    
    path('load-locals/', views.load_locals, name='load_locals'),
    #path('login_success/', views.login_success, name='login-success'),
]
