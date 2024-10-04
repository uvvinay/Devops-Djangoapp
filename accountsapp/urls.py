
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views.home, name="home"),
    path('',views.LOGIN, name='login'),
    path('home', views.home, name="home"),
    path('products/', views.PRODUCTS, name="PRODUCTS"),
    path('orders/', views.ORDERS, name="ORDERS"),
    path('customer/<pk>', views.customer, name='customer'),
    path('register/', views.register, name='register'),
    path('login/', views.LOGIN, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('user/', views.userview, name='user'),
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='accounts/passwordreset.html')),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view()),
    path('<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view()),
    path('reset_done/',auth_views.PasswordResetCompleteView.as_view()),
]
