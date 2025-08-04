from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recommend/', views.run_recommender, name='recommend'),
    path('segment/', views.run_segmentation, name='segment'),
    path('price/', views.run_pricing, name='price'),
]
