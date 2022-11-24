from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:subject>', views.tests, name='tests'),
    #---------------------
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("register/", views.register, name='register')
]
