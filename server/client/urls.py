
from django.urls import path
from .import views

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('viewstore',views.ViewStore,name='viewstore'),
    path('view-inventory',views.ViewInventory,name='view-inventory'),
]

