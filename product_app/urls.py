from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.home2,name="home2"),
    path('registration',views.registration),
    path('log',views.loginview),
    path('userhome',views.display_User,name="userhome"),
    path('log_out',views.logout,name="logout"),
    path('edit',views.display_edit),
    path('update',views.upadte_user),
    path('product',views.display_product,name="producthome"),
    path('product_add',views.addproduct),
    path('search',views.searchproduct),
    path('productupdate',views.updateproduct)
]