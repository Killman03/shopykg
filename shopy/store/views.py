from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
from mptt.models import TreeForeignKey
from mptt.templatetags.mptt_tags import cache_tree_children
from .models import *

menu_header = [{'title': "Доставка", 'url_name': 'delivery', 'img': 'store/images/truck.png'},
               {'title': "Корзина", 'url_name': 'basket', 'img': 'store/images/bin.png'},
               ]

menu_footer = [{'title': "Доставка", 'url_name': 'delivery'},
               {'title': "Продавцам", 'url_name': 'seller'},
               {'title': "О нас", 'url_name': 'aboutus'},
               ]

menu_footer_contact = [{'url_name': 'delivery', 'img': 'store/images/telegram.png'},
                       {'url_name': 'seller', 'img': 'store/images/instagram.png'},
                       {'url_name': 'aboutus', 'img': 'store/images/whatsapp.png'},
                       ]


class HomePage(ListView):
    model = Products
    template_name = 'store/home.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = cache_tree_children(Category.objects.all())
        context['menu_header'] = menu_header
        context['menu_footer'] = menu_footer
        context['menu_footer_contact'] = menu_footer_contact
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Products.objects.filter(is_published=True)


class Collections(ListView):
    model = Category
    template_name = 'store/collections.html'
    context_object_name = 'collections'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Коллекция - ' + str(context['collections'][0].category)

        return context

    def get_queryset(self):
        return Category.objects.filter(category__slug=self.kwargs['collect_slug'], is_published=True)


class Catalog(ListView):
    model = Category
    template_name = 'store/catalog.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        return context

    def get_queryset(self):
        return Category.objects.filter(under_category__slug=self.kwargs['cat_slug'], is_published=True)

class ShowProduct(DetailView):
    model = Products
    template_name = 'store/show_product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_header'] = menu_header
        context['menu_footer'] = menu_footer
        context['menu_footer_contact'] = menu_footer_contact
        context['title'] = str(context['product'].title)
        return context

def delivery(request):
    return HttpResponse('Hi')


def profile(request):
    return HttpResponse('Hi')


def basket(request):
    return HttpResponse('Hi')


def seller(request):
    return HttpResponse('Hi')


def aboutus(request):
    return HttpResponse('Hi')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена [r pf</h1>')

# Create your views here.
