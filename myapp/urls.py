"""
URL configuration for library_project project.

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
from django.urls import path,include
from .import views
from .views import *

urlpatterns = [

#  ======================== Show Messages  =========================
     
    path('', views.home, name='home'),

# ======================== Category =========================
    
    path('category/', category_view.as_view()),
    path('category/<int:id>/', category_view.as_view()),

# ======================== Author ===========================

    path('author/', author_view.as_view()),
    path('author/<int:id>/', author_view.as_view()),
    path('author/category_id/<int:category_id>/', author_view.as_view()),

# ======================== User =============================

    path('user/', user_view.as_view()),
    path('user/<int:id>/', user_view.as_view()),

# ======================== Login User ========================

    path('user_data/', login_user_view.as_view()),
    path('user_data/<int:id>/', login_user_view.as_view()),

# ======================== Admin Login ========================

    path('admin_login/', admin_login_view.as_view()),
    path('admin_login/<int:id>/', admin_login_view.as_view()),
    
# ======================== Book ===============================
    
    path('books/', books_view.as_view()),
    path('books/<int:id>/', books_view.as_view()),

# ======================== Ad ===============================

    path('advertisement/', ad_view.as_view()),
    path('advertisement/<int:id>/', ad_view.as_view()),

# ==================== Notification =========================

    path('notification/', notification_view.as_view()),
    path('notification/<int:id>/', notification_view.as_view()), 

# ==================== Hylighter =========================

    path('hylighter/', hylighter_view.as_view()),
    path('hylighter/<int:id>/', hylighter_view.as_view()),

# =========================== Add Cart Book ================     

    path('add_cart_book/', add_book_view.as_view()),
    path('add_cart_book/<int:id>/', add_book_view.as_view()),

# =========================== Add Wishlist Book ================     

    path('add_wishlist_book/', add_wishlist_book_view.as_view()),
    path('add_wishlist_book/<int:id>/', add_wishlist_book_view.as_view()),


    path('send-email/', send_test_email, name='send_test_email'),
]
