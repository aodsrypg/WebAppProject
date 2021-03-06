"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.hello),
    path('Home/',views.hello),
    path('findRoomPage',views.findRoomPage),
    path('createForm',views.createForm),
    path('addForm',views.addUser),
    path('tableView', views.queryDB),
    path('loginForm', views.loginForm),
    path('login', views.login),
    path('logout', views.logout),
    path('postCard', views.postCard),
    path('postDetail/<slug:Dorm_dormName>', views.postIng),
    path('addPost', views.addPost),
    path('search/',views.search,name='search'),
    path('result',views.result)
]
