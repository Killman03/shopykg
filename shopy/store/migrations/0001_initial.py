# Generated by Django 4.1.7 on 2023-07-06 08:43

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import store.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('meta_title', models.CharField(blank=True, max_length=150)),
                ('meta_keywords', models.CharField(blank=True, max_length=150)),
                ('meta_description', models.CharField(blank=True, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Описание')),
                ('specification', models.CharField(max_length=200, verbose_name='Характеристики')),
                ('image', models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path)),
                ('original_price', models.IntegerField(null=True, verbose_name='Цена')),
                ('selling_price', models.IntegerField(blank=True, null=True, verbose_name='Цена по скидке')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('tag', models.CharField(blank=True, default='#', max_length=150, verbose_name='Teг')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_trending', models.BooleanField(default=False, verbose_name='Хит')),
                ('is_best', models.BooleanField(default=False, verbose_name='Лучшие товары')),
                ('is_new', models.BooleanField(default=False, verbose_name='Новинки')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('under_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='store.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['updated_at'],
            },
        ),
    ]