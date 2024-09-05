from . import views
from django.urls import path 

urlpatterns = [
    
    path('login/',views.loginPage,name='login'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.logoutUser,name='logout'),
]
