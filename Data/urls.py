from django.urls import path 
from . import views
urlpatterns = [


    path("", views.index,name='index'),
    path("index/", views.home,name='home'),
    path("profile/<int:id>", views.profile, name='profile'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
]
