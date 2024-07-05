from django.urls import path

from .views import single_product

urlpatterns = [
    
    path('<slug>/',single_product,name='single_product'),
    


]

