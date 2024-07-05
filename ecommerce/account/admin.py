from django.contrib import admin
from .models import login_page

# admin.site.register(cartItems)

class login_pageadmin(admin.ModelAdmin):
     list_display=['user']
admin.site.register(login_page,login_pageadmin)
