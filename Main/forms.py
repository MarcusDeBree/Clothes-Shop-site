from django.forms import ModelForm
from django import forms
from Main.models import Item, Cart
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Form for add Item to the Site (use Model field - Item)
class AddItemsForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "color", "size_xs", "size_s", "size_m", "size_l", "size_xl",
                  "model", "materials", "country_create", "image", "category_main", "collection"]


# Form for add items to Cart (use Model field - Cart)
class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ["name", "price", "color","size_xs", "size_s", "size_m", "size_l", "size_xl", "image"]


# Form for add User to db (use Model field - User)
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")


# Form for Sign In User to site
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control"}))
