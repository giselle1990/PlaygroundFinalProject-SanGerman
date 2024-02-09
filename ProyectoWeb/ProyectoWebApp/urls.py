from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="Home"),
    path('login', LoginView.as_view(), name="Login" ),
]