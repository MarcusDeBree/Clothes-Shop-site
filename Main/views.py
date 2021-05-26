from django.contrib.auth import login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import generic

from .models import Item, ModelOfItem, PrimaryCategory, Cart
from .forms import AddItemsForm, CartForm, UserRegisterForm, UserLoginForm


# Homepage view
def index(request):
    return render(request, "main/index.html")


# Add page views (only Superuser can see this on site)
def add(request):
    if request.method == "POST":
        form = AddItemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = AddItemsForm
    return render(request, "main/add_item.html", {"form": form})


# Cart page
def cart(request):
    cart_items = Cart.objects.all()
    sum_price = Cart.objects.all().aggregate(Sum('price'))
    return render(request, "main/cart.html", {"cart_items": cart_items, "sum": sum_price})


# Delete page
class DeleteMe(generic.DeleteView):
    template_name = 'main/delete.html'
    model = Cart
    success_url = '/cart'


# Detail of Item
def detail_items(request, pk):
    get_item = Item.objects.get(pk=pk)
    # Need for associate items
    item_collection = Item.objects.all().filter(collection__id=1).filter(model__id = get_item.model.id)
    # When get Detail page increase a count of views (popularity)
    get_item.views += 1
    get_item.save()
    if request.method == "POST":
        cart_form = CartForm(request.POST.copy())
        # Auto complete fields for add Item to cart (create a Cart objects in db)
        cart_form.data["name"] = get_item.name
        cart_form.data["price"] = get_item.price
        cart_form.data["color"]= get_item.color
        cart_form.data["image"] = get_item.image.url
        if cart_form.is_valid():
            cart_form.save()
            return redirect("/cart")
    else:
        cart_form = CartForm()
    return render(request, "main/detail_items.html", {"get_item": get_item, "cart_form": cart_form,
                                                      "item_collection": item_collection})


# List of all items with Primary Category
def list_items(request, pk):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_mans = Item.objects.filter(category_main_id__id=1)
    items_womans = Item.objects.filter(category_main_id__id=2)
    # Pagination (bug: Works only when Mens and Women have pagination.
    # If one of them without pagination - cant see all pages)
    paginator = Paginator(items_mans, 20)
    paginator2 = Paginator(items_womans, 20)
    page = request.GET.get('page')
    page2 = request.GET.get('page')
    try:
        items_m = paginator.page(page)
        items_w = paginator2.page(page2)
    except PageNotAnInteger:
        items_m = paginator.page(1)
        items_w = paginator2.page(1)
    except EmptyPage:
        items_m = paginator.page(paginator.num_pages)
        items_w = paginator2.page(paginator2.num_pages)
    return render(request, "main/list_items.html", {"main_category": main_category, 'items_m': items_m,
                                                    'items_w': items_w })


# List of all items with Primary Category order by price ascending
def list_items_price_asc(request, pk):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_mans = Item.objects.filter(category_main_id__id=1).order_by('-price')
    items_womans = Item.objects.filter(category_main_id__id=2).order_by('-price')
    # Pagination (bug: Works only when Mens and Women have pagination.
    # If one of them without pagination - cant see all pages)
    paginator = Paginator(items_mans, 20)
    paginator2 = Paginator(items_womans, 20)
    page = request.GET.get('page')
    page2 = request.GET.get('page')
    try:
        items_m = paginator.page(page)
        items_w = paginator2.page(page2)
    except PageNotAnInteger:
        items_m = paginator.page(1)
        items_w = paginator2.page(1)
    except EmptyPage:
        items_m = paginator.page(paginator.num_pages)
        items_w = paginator2.page(paginator2.num_pages)
    return render(request, "main/all_items_filter.html", {"main_category": main_category, "items_m": items_m,
                                                          "items_w": items_w})


# List of all items with Primary Category order by price descending
def list_items_price_desc(request, pk):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_mans = Item.objects.filter(category_main_id__id=1).order_by('price')
    items_womans = Item.objects.filter(category_main_id__id=2).order_by('price')
    # Pagination (bug: Works only when Mens and Women have pagination.
    # If one of them without pagination - cant see all pages)
    paginator = Paginator(items_mans, 20)
    paginator2 = Paginator(items_womans, 20)
    page = request.GET.get('page')
    page2 = request.GET.get('page')
    try:
        items_m = paginator.page(page)
        items_w = paginator2.page(page2)
    except PageNotAnInteger:
        items_m = paginator.page(1)
        items_w = paginator2.page(1)
    except EmptyPage:
        items_m = paginator.page(paginator.num_pages)
        items_w = paginator2.page(paginator2.num_pages)
    return render(request, "main/all_items_filter.html", {"main_category": main_category, "items_m": items_m,
                                                          "items_w": items_w})


# List of all items with Primary Category order by views ascending
def views_asc(request, pk):
    main_category = PrimaryCategory.objects.get(id=pk)
    items_mans = Item.objects.filter(category_main_id__id=1).order_by('-views')
    items_womans = Item.objects.filter(category_main_id__id=2).order_by('-views')
    # Pagination (bug: Works only when Mens and Women have pagination.
    # If one of them without pagination - cant see all pages)
    paginator = Paginator(items_mans, 20)
    paginator2 = Paginator(items_womans, 20)
    page = request.GET.get('page')
    page2 = request.GET.get('page')
    try:
        items_m = paginator.page(page)
        items_w = paginator2.page(page2)
    except PageNotAnInteger:
        items_m = paginator.page(1)
        items_w = paginator2.page(1)
    except EmptyPage:
        items_m = paginator.page(paginator.num_pages)
        items_w = paginator2.page(paginator2.num_pages)
    return render(request, "main/all_items_filter.html", {"main_category": main_category, "items_m": items_m,
                                                          "items_w": items_w})


# List of all items with Primary Category order by price descending
def views_desc(request, pk):
    main_category = PrimaryCategory.objects.get(id=pk)
    items_mans = Item.objects.filter(category_main_id__id=1).order_by('views')
    items_womans = Item.objects.filter(category_main_id__id=2).order_by('views')
    # Pagination (bug: Works only when Mens and Women have pagination.
    # If one of them without pagination - cant see all pages)
    paginator = Paginator(items_mans, 20)
    paginator2 = Paginator(items_womans, 20)
    page = request.GET.get('page')
    page2 = request.GET.get('page')
    try:
        items_m = paginator.page(page)
        items_w = paginator2.page(page2)
    except PageNotAnInteger:
        items_m = paginator.page(1)
        items_w = paginator2.page(1)
    except EmptyPage:
        items_m = paginator.page(paginator.num_pages)
        items_w = paginator2.page(paginator2.num_pages)
    return render(request, "main/all_items_filter.html", {"main_category": main_category, "items_m": items_m,
                                                          "items_w": items_w})


# List of items by Model
def list_items_model(request, pk, id):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_model = ModelOfItem.objects.get(pk=id)
    items_mans = Item.objects.filter(category_main_id__id=1).filter(model__id=id)
    items_womans = Item.objects.filter(category_main_id__id=2).filter(model__id=id)

    return render(request, "main/list_items_filter_models.html", {
        "items_model": items_model, 'main_category': main_category,
        "items_mans": items_mans, "items_womans": items_womans
    })


# List of items by Model and order by price ascending
def list_items_price_filter_asc(request, pk, id):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_model = ModelOfItem.objects.get(pk=id)
    items_mans = Item.objects.filter(category_main_id__id=1).filter(model__id=id).order_by('-price')
    items_womans = Item.objects.filter(category_main_id__id=2).filter(model__id=id).order_by('-price')

    return render(request, "main/filter_price.html", {
        "items_model": items_model, 'main_category': main_category,
        "items_mans": items_mans, "items_womans": items_womans
    })


# List of items by Model and order by price descending
def list_items_price_filter_desc(request, pk, id):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_model = ModelOfItem.objects.get(pk=id)
    items_mans = Item.objects.filter(category_main_id__id=1).filter(model__id=id).order_by('price')
    items_womans = Item.objects.filter(category_main_id__id=2).filter(model__id=id).order_by('price')

    return render(request, "main/filter_price.html", {
        "items_model": items_model, 'main_category': main_category,
        "items_mans": items_mans, "items_womans": items_womans
    })


# List of items by Model and order by views ascending
def list_items_views_asc(request, pk, id):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_model = ModelOfItem.objects.get(pk=id)
    items_mans = Item.objects.filter(category_main_id__id=1).filter(model__id=id).order_by('-views')
    items_womans = Item.objects.filter(category_main_id__id=2).filter(model__id=id).order_by('-views')

    return render(request, "main/filter_price.html", {
        "items_model": items_model, 'main_category': main_category,
        "items_mans": items_mans, "items_womans": items_womans
    })


# List of items by Model and order by views descending
def list_items_views_desc(request, pk, id):
    main_category = PrimaryCategory.objects.get(pk=pk)
    items_model = ModelOfItem.objects.get(pk=id)
    items_mans = Item.objects.filter(category_main_id__id=1).filter(model__id=id).order_by('views')
    items_womans = Item.objects.filter(category_main_id__id=2).filter(model__id=id).order_by('views')

    return render(request, "main/filter_price.html", {
        "items_model": items_model, 'main_category': main_category,
        "items_mans": items_mans, "items_womans": items_womans
    })


# Register
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main")
    else:
        form = UserRegisterForm()
    return render(request, "main/register.html", {"form": form})


# Logout
def user_logout(request):
    logout(request)
    return redirect("sign_in")


# Sign in
def sign_in(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("main")
    else:
        form = UserLoginForm()
    return render(request, "main/Sign_in.html", {"form": form})
