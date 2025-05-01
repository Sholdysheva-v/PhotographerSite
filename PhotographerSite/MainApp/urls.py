from django.urls import path
from . import views, converters
from django.urls import register_converter

register_converter(converters.DateOrder, "date_order")

urlpatterns = [
    path('', views.index, name='index'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('delivery/<int:year>/<int:month>/<int:day>/', views.date_delivery, name='delivery_date'),
]


handler404 = 'MainApp.views.page_not_found'