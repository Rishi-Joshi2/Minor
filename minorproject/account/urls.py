from django.urls import path
from django.contrib.auth import views as auth_views
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

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), 
        name="password_reset_complete"),

]