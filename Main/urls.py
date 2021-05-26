from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),  # Homepage
    path('add', views.add, name="add"),  # Add Items to site
    path('cart', views.cart, name="cart"),  # Cart
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteMe.as_view(),
        name='delete'),  # Delete Items from Cart
    path('detail_items/<int:pk>/', views.detail_items,
         name="detail_items"),  # Detail view of Items
    path('list_items/<int:pk>/', views.list_items,
         name="list_items"),  # List of all items by PrimaryCat(Mens or Women)
    path('list_items/<int:pk>/asc_price', views.list_items_price_asc,
         name="list_items_price_asc"),  # List of all items order by price ascending
    path('list_items/<int:pk>/desc_price', views.list_items_price_desc,
         name="list_items_price_desc"),  # List of all items order by price descending
    path('list_items/<int:pk>/asc_views_all', views.views_asc,
         name="views_asc"),  # List of all items order by popularity (views) ascending
    path('list_items/<int:pk>/desc_views_all', views.views_desc,
         name="views_desc"),  # List of all items order by popularity (views) descending
    path('list_items_model/<int:pk>/<int:id>/', views.list_items_model,
         name="list_items_filter_models"),  # List of items Filter by Primary category and Model of Items
    path('list_items_model/<int:pk>/<int:id>/asc', views.list_items_price_filter_asc,
         name="list_items_price_filter_asc"),  # List items with models order by price ascending
    path('list_items_model/<int:pk>/<int:id>/desc', views.list_items_price_filter_desc,
         name="list_items_price_filter_desc"),  # List items with models order by price descending
    path('list_items_model/<int:pk>/<int:id>/asc_views', views.list_items_views_asc,
         name="list_items_views_asc"),  # List items with models order by popularity(views) ascending
    path('list_items_model/<int:pk>/<int:id>/desc_views', views.list_items_views_desc,
         name="list_items_views_desc"),  # List items with models order by popularity(views) descending
    path('register', views.register, name="register"),  # Register
    path('login', views.sign_in, name="sign_in"),  # Login
    path('logout', views.user_logout, name="logout"),  # Logout
]

