from django.db import models
from django.urls import reverse


# Primary category (basic - Man and Woman)
class PrimaryCategory(models.Model):
    name_of_category = models.CharField(max_length=100, verbose_name="основная категория")

    def __str__(self):
        return self.name_of_category


# Model of items (basic - T-shirts & Tanks, Hoodies & Sweatshirts,
# Shorts, Accessories, Jackets & Coats, Sportswear, Shoes, Suits)
class ModelOfItem(models.Model):
    name_model = models.CharField(max_length=100, verbose_name="модель вещи")

    def __str__(self):
        return self.name_model


# Collection of Item (basic - Basics, Bestsellers, Natural) (needed for Cart items associated)
class Collection(models.Model):
    collection_name = models.CharField(max_length=100, verbose_name="коллекция")

    def __str__(self):
        return self.collection_name


# All wear on site
class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование вещи")
    price = models.IntegerField(verbose_name="цена")
    color = models.CharField(max_length=20, verbose_name="цвет")
    size = models.CharField(max_length=1, verbose_name="размер", blank=True, default="")
    size_xs = models.BooleanField(verbose_name="XS", default=False)
    size_s = models.BooleanField(verbose_name="S", default=False)
    size_m = models.BooleanField(verbose_name="M", default=False)
    size_l = models.BooleanField(verbose_name="L", default=False)
    size_xl = models.BooleanField(verbose_name="XL", default=False)
    model = models.ForeignKey(ModelOfItem, on_delete=models.CASCADE, blank=True, verbose_name="модель")
    materials = models.CharField(max_length=255, blank=True, verbose_name="состав")
    country_create = models.CharField(max_length=20, blank=True, verbose_name="страна производитель")
    image = models.ImageField(upload_to="items_photos/", verbose_name="фото вещи")
    category_main = models.ForeignKey(PrimaryCategory, on_delete=models.CASCADE, verbose_name="для кого?")
    date_create = models.DateField(auto_now_add=True, verbose_name="дата создания")
    published = models.BooleanField(default=True, verbose_name="опубликовано?")  # Not Used right now
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True, default="")
    views = models.IntegerField(default=0)

    class Meta:
        get_latest_by = "-date_create"
        ordering = ['-date_create']

    def get_absolute_url(self):
        return reverse("detail_items", args=[str(self.pk)])

    def __str__(self):
        return self.name


# Cart model (fields get from Item, cause form autocomplete with data from Item)
class Cart(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование вещи")
    price = models.CharField(max_length=20, verbose_name="цена с у.е.")
    color = models.CharField(max_length=20, verbose_name="цвет")
    size = models.CharField(max_length=20, verbose_name="размер", blank=True, default="")
    size_xs = models.BooleanField(verbose_name="XS", default=True)
    size_s = models.BooleanField(verbose_name="S", default=True)
    size_m = models.BooleanField(verbose_name="M", default=True)
    size_l = models.BooleanField(verbose_name="L", default=True)
    size_xl = models.BooleanField(verbose_name="XL", default=True)
    image = models.CharField(max_length=1000, verbose_name="фото вещи", default="")

    def __str__(self):
        return self.name

