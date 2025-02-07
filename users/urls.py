from django.urls import path
from users import views

urlpatterns = [
    path('generate_code/', views.generate_code, name='generate_code'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('logout/', views.logout_user, name='logout'),
]
