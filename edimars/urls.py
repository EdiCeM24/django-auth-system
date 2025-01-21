from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('client/', views.client, name='client'),
    path('contact/', views.contact, name='contact'),
    path('forgotPassword/', views.forgotPassword, name='forgot-password'),
    path('send/', views.sendanemail, name='email'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('main/', views.main, name='main'),
    path('member/', views.member, name='member'),
    path('register/', views.register, name='register'),
]