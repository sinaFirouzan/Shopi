from django.urls import path

from products import views

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('get_brands', views.get_brands, name='get_brands'),
    path('get_categories', views.get_categories, name='get_categories'),
]