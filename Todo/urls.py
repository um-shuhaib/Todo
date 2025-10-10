"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TodoApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("register",views.UserRegisterView.as_view(),name="register"),
    path("",views.UserLoginView.as_view(),name="login"),
    path("home",views.HomeView.as_view(),name="home"),
    path("create",views.CreateTodoView.as_view(),name="createtodo"),
    path("delete/<int:id>",views.DeleteView.as_view(),name="delete"),
    path("update/<int:id>",views.UpdateView1.as_view(),name="update"),
    path("logout",views.LogoutView.as_view(),name="logout"),


]
