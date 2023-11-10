
from django.contrib import admin
from django.urls import path, include
from blog import views
urlpatterns = [
    
    # API for handling posts comments
    path('postComment',views.postComment,name='PostComment'),
    path('', views.BlogHome,name='BlogHome'),
    path('<str:slug>', views.BlogPost,name='BlogPost'),
    
]
