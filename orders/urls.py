from django.urls import path
from .views import create_order
from django.utils.translation import gettext_lazy as _

app_name = 'order'

urlpatterns = [
    path(_('create/'), create_order, name='order_create')
]
