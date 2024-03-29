from django.urls import path
from . import views

urlpatterns = [
    path('test', views.Test.as_view(), name='test'),
    path('', views.Main.as_view(), name='main'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('register', views.Register.as_view(), name='register'),
    path('home', views.Home.as_view(), name='home'),
    path('chatting', views.Chatting.as_view(), name='chatting'),
]
