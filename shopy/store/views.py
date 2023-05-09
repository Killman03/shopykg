from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse
from django.views.generic import ListView
from .models import *

menu_header = [{'title': "Доставка", 'url_name': 'delivery'},
        {'title': "Войти", 'url_name': 'profile'},
        {'title': "Корзина", 'url_name': 'basket'},
        ]

menu_footer = [{'title': "Доставка", 'url_name': 'delivery'},
        {'title': "Продавцам", 'url_name': 'seller'},
        {'title': "О нас", 'url_name': 'aboutus'},
        ]

class Collections(ListView):
    model = Under_category
    template_name = 'store/collections.html'
    context_object_name = 'collections'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Коллекция - ' + str(context['collections'][0].category)

        return context

    def get_queryset(self):
        return Under_category.objects.filter(category__slug=self.kwargs['slug'], is_published=True)

def home(request):
    return render(request, 'store/home.html', {'menu': menu_footer})

def catalog(request):
    return render(request, 'store/catalog.html')

def show_product(request, product_slug):
    product = get_object_or_404(Articles, slug=product_slug)
    context = {'product': product,
               'menu': menu,
               'title': product.title,
               'category_name': product.category}

    return render(request, 'store/products/index.html', context=context)

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