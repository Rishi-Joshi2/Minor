from django.urls import path
from .import views

urlpatterns = [
    path("login_register_form", views.logReg, name = 'logReg'),
    path("login/", views.login, name = 'login'),
    path("signup/", views.signup, name = 'signup'),
    path("logout/", views.logout, name = 'logout'),
    path("user_information/",views.user_information, name='user_information'),
    path("invoices/",views.invoices, name='invoices'),
    path("address/",views.address, name='address'),
    path("edit_address/",views.edit_address, name='edit_address'),
]