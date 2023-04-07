from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('home/', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('mobile/', views.mobile, name="mobile"),
    path('electronics/', views.electronics, name="electronics"),
    path('essential/', views.essential, name="essential"),
    path('fashion/', views.fashion, name="fashion"),
    path('top_offers/', views.top, name="top"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]