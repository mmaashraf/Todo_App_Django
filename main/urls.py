"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

from django.urls import path

from . import views #this will be usefull when we want to include certain urls,instead of hardcoding it we can use views.

app_name="main"

urlpatterns = [
   path("",views.homepage,name="homepage"),#call the homepage fucntion in views.py
   path("register/",views.register,name="register"),
   path("logout/",views.logout_user,name="logout"),
   path("login/",views.login_user,name="login"),
   path("viewlist/",views.viewlist,name="viewlist"),
    path("list/", views.book_list, name="book_list"),
   path("new/", views.book_create, name="book_new"),
   path("edit/<int:pk>/", views.book_update, name="book_edit"),
   path("delete/<int:pk>/", views.book_delete, name="book_delete"),
]
