from django.urls import path

from . import views
urlpatterns = [
    # Leave as empty string for base url
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('service/', views.service, name="service"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('user_design/', views.user_designs, name="user_design"),
]
