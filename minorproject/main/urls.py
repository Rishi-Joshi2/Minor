from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name = 'home'),
    path("about_us",views.aboutus, name = 'aboutus'),
    path("policy",views.policy, name = 'policy'),
    path("terms_condition",views.termsCondition, name = 'termsCondition'),
    path("shipping",views.shipping, name = 'shipping'),
    path("contact_us",views.contactUs, name = 'contactUs'),
    path("cart",views.cart1, name = 'cart'),
    path("checkout",views.checkout, name = 'checkout'),
    path("categories",views.categories, name = 'categories'),
    path("product_details/<int:pk>",views.product_details, name = 'product_details'),
    path("add_to_cart/", views.add_to_cart),
    path("minus_cart/",views.minus_cart),
    path("removecart/",views.removecart),
]