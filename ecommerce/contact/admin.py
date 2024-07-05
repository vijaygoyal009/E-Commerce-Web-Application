from django.contrib import admin
from .models import contact

# Register your models here.
class contactadmin(admin.ModelAdmin):
    list_display=['user','E_mail']
admin.site.register(contact,contactadmin)
