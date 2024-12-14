from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'), 
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('delprofile/<id>/',views.delprofile,name='delprofile'),
    path('shopindex/',views.shopindex,name='shopindex'),
    path('shopregister/',views.shopreg,name='shopregister'),
    path('shoplogin/',views.shoplogin,name='shoplogin'),
    path('shopviewprofile/',views.shopviewprofile,name='shopviewprofile'),
    path('shopeditprofile/',views.shopeditprofile,name='shopeditprofile'),
    path('shopdelprofile/<id>/',views.shopdelprofile,name='shopdelprofile'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('viewproduct/',views.viewproduct,name='viewproduct'),
    path('editproduct/<id>/',views.editproduct,name='editproduct'),
    path('delproduct/<id>/',views.delproduct,name='delproduct'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('users/', views.user_list_view, name='user_list'),  # for all users
    path('shopslist/', views.shop_list_view, name='shop_list'),  
    path('productslist/', views.product_list_view, name='product_list'), 
    path('userlistedit/<uid>/', views.userlist_editprofile, name='userlistedit'), 
    path('userlistdel/<uid>/', views.userlist_delprofile, name='userlistdel'), 
    path('shoplistedit/<uid>/', views.shopslist_editprofile, name='shoplistedit'), 
    path('shoplistdel/<uid>/', views.shopslist_delprofile, name='shoplistdel'), 
]
