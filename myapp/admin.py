from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(category)

admin.site.register(author)

admin.site.register(user)

admin.site.register(login_user)

admin.site.register(admin_login)

admin.site.register(Books)

admin.site.register(hylighter)

admin.site.register(add_book)

admin.site.register(wishlist)