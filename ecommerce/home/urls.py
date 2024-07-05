"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import index,search,pluscart,removecart,minuscart,about,showcart,blog,cart1,contact1,shop

urlpatterns = [
   
    path('',index,name='home'),
     path('about/',about,name='about'),

     
     
      path('pluscart/',pluscart,name='pluscart'),
        path('minuscart/',minuscart,name='minuscart'),
           path('removecart/',removecart,name='removecart'),
       path('blog/',blog,name='blog'),

          path('contact/',contact1,name='contact'),
           path('shop/',shop,name='shop'),
         path('cart1/',cart1,name="cart1"),
         path('showcart/',showcart,name='showcart'),
             path('search/',search,name='search'),
         

    
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
