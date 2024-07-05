from django.db import models
from django.contrib.auth.models import User
from product.models import product,Coupon,colorvariant,sizevariant
from django.core.validators import MinValueValidator

# Create your models here.
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='cart1')
    coupon=models.ForeignKey(Coupon,on_delete=models.SET_NULL,null=True,blank=True)
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1,validators=[MinValueValidator(1)]) 
    razor_pay_order_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_id=models.CharField(max_length=100,null=True,blank=True)
    razor_pay_payment_signature=models.CharField(max_length=100,null=True,blank=True) 
    def get_cart_total(self):
         cart_items=self.cart_items.all()
         price=[]
         for cart_item in cart_items:
              price.append(cart_item.product_id.price)
              if cart_item.color_variant:
                   color_variant_price=cart_item.color_variant_price
                   price.append(color_variant_price)
              if cart_item.size_variant:
                   size_variant_price=cart_item.size_variant_price
                   
                   price.append(size_variant_price)
         print(sum(price))
         return sum(price)
class abc1(models.Model):
    cartname=models.ForeignKey(cart, on_delete=models.CASCADE, related_name='cart_items')
    product_id=models.ForeignKey(product, on_delete=models.CASCADE)
    color_variant=models.ForeignKey(colorvariant,on_delete=models.SET_NULL,null=True)
    size_variant=models.ForeignKey(sizevariant,on_delete=models.SET_NULL,null=True)
    
    def get_product_price(self):
        price=[self.product_id.price]
        if self.size_variant:
                size_variant_price=self.size_variant.price
                price.append(size_variant_price)
        if self.color_variant:
             color_variant_price=self.color_variant.price
             price.append(color_variant_price)
        return sum(price)
   
   
