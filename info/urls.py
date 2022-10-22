from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('update_active/', views.update_active, name='update_active'),
    path('update_content/', views.update_content, name='update_content'),
]