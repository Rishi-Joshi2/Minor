from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name = 'home'),
    path("about_us",views.aboutus, name = 'aboutus'),
    path("policy",views.policy, name = 'policy'),
    path("terms_condition",views.termsCondition, name = 'termsCondition'),
    path("shipping",views.shipping, name = 'shipping'),
    path("contact_us",views.contactUs, name = 'contactUs'),
]