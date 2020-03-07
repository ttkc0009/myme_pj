"""myme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
# from . import view_other

urlpatterns = [
    path('', views.show_home, name="show_home"),
    path('other/chat', views.show_other, name="show_chat"),
    path('about', views.show_about, name="show_about"),
    path('news', views.show_news, name="show_news"),
    path('blog', views.show_blog, name="show_blog"),
    path('access', views.show_access, name="show_access"),
    path('other', views.show_other, name="show_other"),
    # path('other/chat', view_other.show_chat, name="show_chat"),
]
