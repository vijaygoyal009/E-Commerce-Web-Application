from django.db import models
from django.utils.text import slugify

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,blank=True,null=True)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.category_name)
        super(category,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.category_name
class  colorvariant(models.Model):
    color_name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.color_name
class sizevariant(models.Model):
    size_name=models.CharField(max_length=100,default='M')
    price=models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.size_name
    
class product(models.Model):
    product_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,blank=True,null=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE,related_name='category1')
    price=models.IntegerField()
    description=models.TextField()
    color_variant=models.ManyToManyField(colorvariant,blank=True)
    size_variant=models.ManyToManyField(sizevariant,blank=True)
    product_image=models.ImageField(upload_to="product_img")
    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_name)
        super(product,self).save(*args,**kwargs)
    
    def __self__(self):
        return self.product_name
    def get_product_price_by_size(self,size):
        return self.price + sizevariant.objects.get(size_name=size).price



  
class Coupon(models.Model):
    coupon_code=models.CharField(max_length=100)
    is_expired=models.BooleanField(default=False)
    discount_price=models.IntegerField(default=100)
    minimum_amount=models.IntegerField(default=500)
