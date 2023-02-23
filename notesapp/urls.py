"""notesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from notes import views
from django.urls import path, re_path
from notes.forms import SignInForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.sign_up, name="signup"),
    path('signin/', views.sign_in, name='signin'),
    path('signout/', views.sign_out, name='signout'),
    path("", views.index, name="index"),
    re_path(r'^mynotes/$', views.mynotes, name='mynotes'),
    re_path(r'^note/(?P<pk>\d+)$', views.NoteDetail.as_view(), name='note-detail'),
    path("mynotes/api/search/", views.search, name="search"),
    path("mynotes/api/delete/", views.delete, name="delete")
]
