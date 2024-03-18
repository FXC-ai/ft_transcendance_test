"""
URL configuration for bck_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from members_test_fx import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('hello/', views.hello, name='hello'),
    path('hello/<int:id>/', views.hello_details, name='hello-details'),
	path('subscribe/', views.subscribe),
	path('email-sent/', views.email_sent, name='email-sent'),
	path('games/add/', views.game_create, name='games-create'),
	path('games/<int:id>/change/', views.game_change, name='games-change'),
	path('games/<int:id>/delete/', views.game_delete, name='games-delete'),
]
