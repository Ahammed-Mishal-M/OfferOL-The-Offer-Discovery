from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(unique=True,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    gender_choices=(
        ('MALE','male'),
        ('FEMALE','female'),
        ('OTHERS','others')
        
    )
    gender=models.CharField(choices=gender_choices,max_length=10)
    age=models.IntegerField(null=True,blank=True)
    password=models.CharField(max_length=8,null=True,blank=True)
    image=models.ImageField(upload_to='user/',null=True,blank=True)
    def __str__(self):
        return self.name

class shopregister(models.Model):
    shopname=models.CharField(max_length=50,null=True,blank=False)
    shopownername=models.CharField(max_length=50,null=True,blank=False)
    email=models.EmailField(unique=True,null=True,blank=False)
    phone=models.IntegerField(null=True,blank=True)
    storeid=models.CharField(max_length=50,null=True,blank=False,unique=True)
    password=models.CharField(max_length=8,null=True,blank=True)
    image=models.ImageField(upload_to='shop/',null=True,blank=True)
    location=models.CharField(max_length=50,null=True,blank=False)
    def __str__(self):
        return self.shopname

class product(models.Model):
    productname=models.CharField(max_length=50,null=True,blank=False)
    productimage=models.ImageField(upload_to='product/',null=True,blank=True) 
    productprice=models.IntegerField(null=True,blank=True)
    offerprice=models.DecimalField(max_digits=100,null=True,blank=True,decimal_places=2) 
    discountvalue=models.IntegerField(null=True,blank=True) 
    stock=models.IntegerField(null=True,blank=True) 
    shopname=models.ForeignKey(shopregister,on_delete=models.CASCADE)

class adminregister(models.Model):
   username=models.CharField(max_length=50,null=True,blank=True)
   email=models.EmailField(unique=True,null=True,blank=True)
   password=models.CharField(max_length=8,null=True,blank=True)
   def __str__(self):
        return self.username
 


    

     

    