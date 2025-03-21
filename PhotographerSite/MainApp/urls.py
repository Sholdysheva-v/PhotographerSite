from django.urls import path
from . import views, converters
from django.urls import register_converter

register_converter(converters.DateOrder, "date_order")

urlpatterns = [
    path('', views.index, name='home'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('orders/<date_order:date>/', views.date_order, name='date_order'),
]
