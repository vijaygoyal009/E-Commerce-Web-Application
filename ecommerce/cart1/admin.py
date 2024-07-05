from django.contrib import admin
from .models import cart#,cartItems

# Register your models here.
class cartadmin(admin.ModelAdmin):
    list_display=['user','product_id','quantity']
admin.site.register(cart,cartadmin)

