from store.views import *
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('delivery/', delivery, name='delivery'),
    path('profile/', profile, name='profile'),
    path('basket/', basket, name='basket'),
    path('seller/', seller, name='seller'),
    path('aboutus/', aboutus, name='aboutus'),
    path('collections/<slug:slug>/', Collections.as_view(), name='collection'),
    path('product/<str:product_slug>/', show_product, name='product'),
]