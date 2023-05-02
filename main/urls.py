from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path("reg2/", views.frontend_register, name="register2"),
    path("login/",  LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("login2/", views.frontend_login, name="login2")
]