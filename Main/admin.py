from django.contrib import admin
from .models import *


# Admin Item model panel
@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    ordering = ['-date_create']
    date_hierarchy = 'date_create'
    list_display = ('name', 'price', 'color', 'category_main', 'date_create', 'published', 'views')
    list_filter = ('price', 'published', 'category_main', 'date_create')
    search_fields = ['name']
    show_full_result_count = True


# Admin Model of Item model panel
@admin.register(ModelOfItem)
class ModelsAdmin (admin.ModelAdmin):
    list_display = ('name_model',)


# Admin Item model panel
@admin.register(Cart)
class CartAdmin (admin.ModelAdmin):
    list_display = ('name',)


# Admin Primary Category
@admin.register(PrimaryCategory)
class PrimaryCatAdmin(admin.ModelAdmin):
    list_display = ('name_of_category',)


# Admin Collection
@admin.register(Collection)
class CollectionAdmin (admin.ModelAdmin):
    list_display = ('collection_name',)
