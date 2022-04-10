from django.views.generic import RedirectView
from django.urls import path
from store import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('favicon\.ico',RedirectView.as_view(url='/static/images/favicon.ico')),
]
