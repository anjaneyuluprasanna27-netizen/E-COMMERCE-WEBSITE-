from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/cart/add/', views.cart_add, name='cart_add'),
    # The documentation references these views, but their implementations
    # were not included in the uploaded document.
    # path('api/cart/update/', views.cart_update, name='cart_update'),
    # path('api/cart/remove/', views.cart_remove, name='cart_remove'),
    # path('api/cart/state/', views.cart_state, name='cart_state'),
    path('api/checkout/', views.checkout, name='checkout'),
]
