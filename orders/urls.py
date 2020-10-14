from django.urls import path
from .views import create_order

app_name = 'order'

urlpatterns = [
    path('create/', create_order, name='order_create')
]
