
from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    
    path('', views.home,name='Home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('search/', views.search,name='search'),
    path('signUp/', views.signUp,name='signup'),
    path('login/', views.loginHand,name='login'),
    path('logout/', views.logoutHand,name='logout')
    
]
