from django.shortcuts import render,HttpResponse,redirect
from app.models import Register,shopregister,product,adminregister
from django.contrib.auth.models import User 


# Create your views here.
#user
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        age=request.POST.get('age')
        image=request.FILES.get('image')
        gender=request.POST.get('gender')
        if Register.objects.filter(email=email).exists():
            alert="<script>alert('email already exist');window.location.href='/register';</script>"
            return HttpResponse(alert)
        obj=Register(name=name,email=email,phone=phone,password=password,age=age,image=image,gender=gender)
        obj.save()
        return redirect('home')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            us=Register.objects.get(email=email,password=password)
            semail=us.email
            request.session['email']=semail
            return redirect('index')
        except:
            msg="invalid username or password" 
        return render(request,'login.html',{"msg":msg})
    return render(request,'login.html')  
     
def viewprofile(request):
    try:
        email=request.session['email']
        user=Register.objects.get(email=email)
        if user:
            return render(request,'viewprofile.html',{'usr':user})
        else:
            return redirect('login')
    except:
        return redirect('login') 

def editprofile(request):
    email=request.session['email']
    user=Register.objects.get(email=email)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        age=request.POST.get('age')
        image=request.FILES.get('image')
        gender=request.POST.get('gender')

        user.name=name
        user.email=email
        user.phone=phone
        user.password=password
        user.age=age
        if image:
            user.image=image
        user.gender=gender
        user.save()
        return redirect('viewprofile')
    return render(request,'editprofile.html',{'usr':user})

def delprofile(request,id):
    user=Register.objects.get(id=id)
    user.delete()
    return redirect('index')

#shopowner

def shopindex(request):
    return render(request,'shopindex.html')

def shopreg(request):
    if request.method=="POST":
        shopname=request.POST.get('shopname')
        shopownername=request.POST.get('shopownername')
        storeid=request.POST.get('storeid')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        location=request.POST.get('location')
        if shopregister.objects.filter(email=email).exists():
            alert="<script>alert('email already exist');window.location.href='/shopregister';</script>"
            return HttpResponse(alert)
        obj=shopregister(shopname=shopname,shopownername=shopownername,email=email,phone=phone,password=password,image=image,location=location)
        obj.save()
        return redirect('home')
    return render(request,'shopregister.html')

def shoplogin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            us=shopregister.objects.get(email=email,password=password)
            semail=us.email
            request.session['semail']=semail
            return redirect('index')
        except:
            msg="invalid username or password" 
        return render(request,'shoplogin.html',{"msg":msg})
    return render(request,'shoplogin.html')  
     
def shopviewprofile(request):
    try:
        email=request.session['semail']
        shop=shopregister.objects.get(email=email)
        if shop:
            return render(request,'shopviewprofile.html',{'shop':shop})
        else:
            return redirect('shoplogin')
    except Exception as e:
        print (e)
        return redirect('shoplogin')  

def shopeditprofile(request):
    email=request.session['semail']
    try:

        shop=shopregister.objects.get(email=email)
    except  :
        return redirect('shoplogin')
    if request.method=="POST":
        shopname=request.POST.get('shopname')
        shopownername=request.POST.get('shopownername')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        storeid=request.POST.get('storeid')
        image=request.FILES.get('image')
        location=request.POST.get('location')

        shop.shopname=shopname
        shop.shopownername=shopownername
        shop.email=email
        shop.phone=phone
        shop.password=password
        shop.storeid=storeid
        shop.location=location
        if image:
            shop.image=image
        shop.save()
        return redirect('shopviewprofile')
    return render(request,'shopeditprofile.html',{'shop':shop})

def shopdelprofile(request,id):
    shop=shopregister.objects.get(id=id)
    shop.delete()
    return redirect('shopindex')

def addproduct(request):
    email=request.session['semail']
    try:
        shop=shopregister.objects.get(email=email)
    except  :
        return redirect('shoplogin')
    if request.method=='POST':
        productname=request.POST.get('productname')
        productimage=request.FILES.get('productimage')
        productprice=request.POST.get('productprice')
        offerprice=request.POST.get('offerprice')
        discountvalue=request.POST.get('discountvalue')
        stock=request.POST.get('stock')
        obj=product(productname=productname,productimage=productimage,productprice=productprice,offerprice=offerprice,discountvalue=discountvalue,stock=stock,shopname=shop)
        obj.save()
        return redirect('home')
    return render(request,'addproduct.html')
        
        
def viewproduct(request):
    try:
        email=request.session['semail']
        shop=product.objects.filter(shopname__email=email)
        if shop:
            return render(request,'viewproduct.html',{'shop':shop})
        else:
            return redirect('shoplogin')
    except Exception as e:
        print (e)
        return redirect('shoplogin') 

def editproduct(request,id):
    email=request.session['semail']
    try:

        shop=product.objects.get(shopname__email=email,id=id)
    except  :
        return redirect('shoplogin')
    if request.method=="POST":
        productname=request.POST.get('productname')
        productimage=request.FILES.get('productimage')
        productprice=request.POST.get('productprice')
        offerprice=request.POST.get('offerprice')
        discountvalue=request.POST.get('discountvalue')
        stock=request.POST.get('stock')

        shop.productname=productname
        shop.productprice=productprice
        shop.offerprice=offerprice
        shop.discountvalue=discountvalue
        shop.stock=stock
        if productimage:
            shop.productimage=productimage
        shop.save()
        return redirect('viewproduct')
    return render(request,'editproduct.html',{'shop':shop})        

def delproduct(request,id):
    shop=product.objects.get(id=id)
    shop.delete()
    return redirect('viewproduct')

#admin section

def adminindex(request):
    return render(request,'adminindex.html') 


def adminlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            adm=adminregister.objects.get(email=email,password=password)
            if adm:
                request.session['ademail']=adm.email
                return redirect('adminindex')
            else:
                return redirect('adminlogin') 
        except:
            return redirect('adminlogin')
    return render(request,'adminlogin.html')   

def home(request):
    return render(request,'home.html')
  

  
def user_list_view(request):
    if 'ademail' in request.session:
        users = Register.objects.all()  
        return render(request, 'users.html', {'users': users})
    else:
        return redirect('adminlogin')    

def shop_list_view(request):
    if 'ademail' in request.session:
        shopslist = shopregister.objects.all()  
        return render(request, 'shopslist.html', {'shopslist': shopslist})
    else:
        return redirect('adminlogin')          

def product_list_view(request):
    if 'ademail' in request.session:
        productslist = product.objects.all()  
        return render(request, 'productslist.html', {'productslist': productslist})
    else:
        return redirect('adminlogin')    



def userlist_editprofile(request,uid):
    user=Register.objects.get(id=uid)
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        age=request.POST.get('age')
        image=request.FILES.get('image')
        gender=request.POST.get('gender')

        user.name=name
        user.email=email
        user.phone=phone
        user.password=password
        user.age=age
        if image:
            user.image=image
        user.gender=gender
        user.save()
        return redirect('adminindex')
    return render(request,'editusers.html',{'users':user})


def userlist_delprofile(request,uid):
    user=Register.objects.get(id=uid)
    user.delete()
    return redirect('user_list') 


def shopslist_editprofile(request,uid):
    # email=request.session['semail']
    try:
        shop=shopregister.objects.get(id=uid)
    except  :
        return redirect('shoplistedit')
    if request.method=="POST":
        shopname=request.POST.get('shopname')
        shopownername=request.POST.get('shopownername')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        storeid=request.POST.get('storeid')
        image=request.FILES.get('image')
        location=request.POST.get('location')

        shop.shopname=shopname
        shop.shopownername=shopownername
        shop.email=email
        shop.phone=phone
        shop.password=password
        shop.storeid=storeid
        shop.location=location
        if image:
            shop.image=image
        shop.save()
        return redirect('adminindex')
    return render(request,'editshops.html',{'shop':shop})

def shopslist_delprofile(request,uid):
    shop=shopregister.objects.get(id=uid)
    shop.delete()
    return redirect('shop_list')
