from django.urls import path, include
from . import views





app_name = 'slugapp'





urlpatterns = [
    path('', views.postList, name ='post_list'),
    path('<slug:slug>/', views.postDetails, name ='post_detail'),
    
]

