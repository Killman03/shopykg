from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from PIL import Image
import datetime
import os

def get_file_path(request, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (now_time, original_filename)
    return os.path.join('images/', filename)

class Category(models.Model):
    title = models.CharField('Название', max_length=30, null=False, blank=False)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=True)
    meta_keywords = models.CharField(max_length=150, null=False, blank=True)
    meta_description = models.CharField(max_length=150, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        ordering = ['updated_at']
        verbose_name_plural = 'Категории'

class Under_category(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.PROTECT)
    title = models.CharField('Название', max_length=30, null=False, blank=False)
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    category_image = models.ImageField('Изображение', upload_to=get_file_path, null=True, blank=True)
    trending = models.BooleanField(default=False)
    meta_title = models.CharField(max_length=150, null=False, blank=True)
    meta_keywords = models.CharField(max_length=150, null=False, blank=True)
    meta_description = models.CharField(max_length=150, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('undercategory', kwargs={'undercategory_slug': self.slug})

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['updated_at']

class Products(models.Model):
    under_category = models.ForeignKey(Under_category, default=1, on_delete=models.PROTECT)
    title = models.CharField('Название', max_length=30, null=False, blank=False)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField('Описание', blank=False)
    specification = models.CharField('Характеристики', max_length=200, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    original_price = models.IntegerField('Цена', null=True, blank=False)
    selling_price = models.IntegerField('Цена по скидке', null=True, blank=True)
    quantity = models.IntegerField('Количество', null=True, blank=True)
    tag = models.CharField('Teг', max_length=150, default='#', null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_trending = models.BooleanField('Хит', default=False)
    is_best = models.BooleanField('Лучшие товары', default=False)
    is_new = models.BooleanField('Новинки', default=False)
    is_published = models.BooleanField('Опубликовать', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['updated_at']
