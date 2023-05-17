from store.views import *
from django.urls import path


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('delivery/', delivery, name='delivery'),
    path('profile/', profile, name='profile'),
    path('basket/', basket, name='basket'),
    path('seller/', seller, name='seller'),
    path('aboutus/', aboutus, name='aboutus'),
    path('collections/<slug:collect_slug>/', Collections.as_view(), name='collection'),
    path('collections/<slug:slug>/<slug:cat_slug>/', Catalog.as_view(), name='catalog'),
    path('collections/<slug:slug>/<slug:cat_slug>/<slug:product_slug>/', ShowProduct.as_view(), name='product'),
]