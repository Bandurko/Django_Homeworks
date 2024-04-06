from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),  # вывод главной страницы
    path('client_orders/<int:id_client>', views.client_orders, name='client_orders'),
    # все заказы клиента
    path('shop/client_products_sorted/<int:id_client>/<int:days>/', views.client_products_sorted,
         name='client_products_sorted'),
    # вывод всех товаров по клиенту за указанное кол дней
]