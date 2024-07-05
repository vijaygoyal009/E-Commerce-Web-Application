from django.shortcuts import render
from .models import product
from django.contrib.auth.decorators import login_required
@login_required(login_url='/account/login1/')
def single_product(request,slug):
  try:
     products=product.objects.get(slug=slug)
     context={'products':products }
    
     if request.GET.get('size'):
      size=request.GET.get('size')
      price=products.get_product_price_by_size(size)
      context['selected_size']=size
      context['updated_price']=price
      
    

     return render(request,'single-product.html',context=context)
  except Exception as e:
     print(e) 
   #     return render(request,'single-product.html')


    

