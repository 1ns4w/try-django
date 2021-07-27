from django.urls import path
from . import views

urlpatterns = [

    # These are static URLs routes to views
    path('', views.index, name = "index"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('counter', views.counter, name = "counter"),
    path('logout', views.logout, name = "logout"),

    # These are dynamic URLs routes to views
    path('post/<str:pk>', views.post, name = "post"),
]