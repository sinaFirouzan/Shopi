from django.urls import path

from banners import views

urlpatterns = [
    path('banners/', views.get_banners, name='banner_slider'),
    path('categories/', views.get_category_slider, name='category_slider'),
    path('brands/', views.get_brand_slider, name='brand_slider'),
]