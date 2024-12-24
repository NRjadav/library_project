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
    path('user_data/<str:id>/', login_user_view.as_view()),
    path('user_data/email/<str:email>/', login_user_view.as_view()),

# ======================== Admin Login ========================

    path('admin_login/', admin_login_view.as_view()),
    path('admin_login/<int:id>/', admin_login_view.as_view()),

# =========================== Languages ================     

    path('languages/', languages_view.as_view()),
    path('languages/<int:id>/', languages_view.as_view()),

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

    path('hylighter1/', hylighter_view1.as_view()),
    path('hylighter1/<int:id>/', hylighter_view1.as_view()),
    path('hylighter1/user_id/<str:user_id>/book_id/<int:book_id>', hylighter_view1.as_view()),

# =========================== Add Cart Book ================     

    path('add_cart_book/', add_book_view.as_view()),
    path('add_cart_book/<int:id>/', add_book_view.as_view()),

# =========================== Add Wishlist Book ================     

    path('add_wishlist_book/', add_wishlist_book_view.as_view()),
    path('add_wishlist_book/<int:id>/', add_wishlist_book_view.as_view()),



    path('send-email/', send_test_email, name='send_test_email'),


    path('hylighter1/user_id/<str:user_id>/book_id/<int:book_id>/word_id/<int:word_id>/delete/', HylighterDeleteWordView.as_view(), name='delete_highlighter_word'),
    path('hylighter1/<str:user_id>/<int:book_id>/', HylighterDeleteWordView.as_view())
]



"""

post and patch book new formate

{
        
        "author_data": [
           1,2                                # <- author ID
        ],
        "category_data": [
          3                                   # <- category ID
        ],
        "language_data": [
          1                                   # <- language ID
        ],

        "book_keywords": [
            "Python", "Python", "Python"
           
        ],
       
        
        "book_front_image": "/image/2cb1fc130a3f12398ad5.jpg",
        "book_file": null,    # <- epup file upload in form data
        "book_name_english": "python",
        "book_name_hindi": "aaa",
        "book_details_english": "1",
        "book_details_hindi": "4",
        "book_price_discount": 1,
        "book_price": 1.0,
        "book_free_demo": 0.0,
        "purchase": false
    }


"""