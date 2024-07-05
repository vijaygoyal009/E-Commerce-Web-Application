from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Coupon)
admin.site.register(category)

class productadmin(admin.ModelAdmin):
    list_display=['product_name','price']
    

class colorvariantadmin(admin.ModelAdmin):
    list_display=['color_name','price']
    model=colorvariant
class sizevariantadmin(admin.ModelAdmin):
    list_display=['size_name','price']
    model=sizevariant
admin.site.register(colorvariant,colorvariantadmin)
admin.site.register(sizevariant,sizevariantadmin)

admin.site.register(product,productadmin)
# admin.site.register(productimage)
