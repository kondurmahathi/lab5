"""
URL configuration for blog_project project.

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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# blog_project/urls.py
# blog_project/urls.py
# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth.views import LogoutView  # Import LogoutView
# from blog.views import profile  # Import the profile view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('register/', include('blog.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/profile/', profile, name='profile'),  # Use the profile view
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('', include('blog.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView  # Import LogoutView
from blog.views import profile  # Import the profile view
from blog.views import logout_view
from blog.views import custom_login
from blog.views import post_list
from blog.views import search, other_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='profile'),  # Use the profile view
    path('logout/', logout_view, name='logout'),
    path('', include('blog.urls')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('accounts/login/', custom_login, name='custom_login'),
    path('post-list/', post_list, name='post_list'),
    path('search/', search, name='search'),
    path('other/', other_view, name='other_view'),
]
