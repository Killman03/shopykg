from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse
from django.views.generic import ListView
from django.views.generic import DetailView
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
        context['menu_header'] = menu_header
        context['menu_footer'] = menu_footer
        context['menu_footer_contact'] = menu_footer_contact
        context['title'] = 'Главная страница'
        context['category'] = Under_category.objects.get(title='Комбо')
        return context

    def get_queryset(self):
        return Products.objects.filter(is_published=True)


class Collections(ListView):
    model = Under_category
    template_name = 'store/collections.html'
    context_object_name = 'collections'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Коллекция - ' + str(context['collections'][0].category)

        return context

    def get_queryset(self):
        return Under_category.objects.filter(category__slug=self.kwargs['collect_slug'], is_published=True)


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
        context = super().(**kwargs)
        context['menu_header'] = menu_header
        context['menu_footer'] = menu_footer
        context['menu_footer_contact'] = menu_footer_contact
        context['title'] = str(context['product'].title)
        return context


# def show_product(request, product_slug):
#     product = get_object_or_404(Articles, slug=product_slug)
#     context = {'product': product,
#                'menu': menu,
#                'title': product.title,
#                'category_name': product.category}
#
#     return render(request, 'store/bootstrap/index.html', context=context)

# def collections(request, collections_slug):
#     collections = get_object_or_404(Under_category, slug=collections_slug)
#     context = {'collections': collections,
#                'menu': menu,
#                'title': collections.title,
#                'category_name': collections.category}
#
#     return render(request, 'store/collections.html', context=context)

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
