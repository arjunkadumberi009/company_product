import email
from django.shortcuts import render
from .models import user_reg,product_details
from .forms import ConsumerForm,loginForm,productForm


# Create your views here.
def home(request):
    return render(request,"User/home.html")

def home2(request):
    form=ConsumerForm   
    form1=loginForm
    return render(request,"User/login.html",{"form":form,"form1":form1})


#registration of staff
def registration(request):
    submitted=False
    message={}
    form=ConsumerForm
    form1=loginForm
    if request.method=='POST':
        form=ConsumerForm(request.POST)
        if form.is_valid():
            fname=request.POST['first_name']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            if password==confirm_password:
                if user_reg.objects.filter(first_name=fname).exists():
                    return render(request,"User/login.html",{"form":form,"form1":form1,'msg1':"Name already taken"})
                if user_reg.objects.filter(email=email).exists():
                    return render(request,"User/login.html",{"form":form,"form1":form1,'msg3':"Email already taken"})
                else:
                    form.save()
                    submitted=True
                    return render(request,"User/login.html",{'submitted':submitted,"form1":form1})
        return render(request,"User/login.html",{'submitted':submitted,"form":form,"form1":form1})

#Login of staff
def loginview(request):
    message={}
    form=ConsumerForm
    form1=loginForm
    if request.method=='POST':
        form1=loginForm(request.POST)
        if form1.is_valid():
            name=request.POST['first_name']
            password=request.POST['password']
            if user_reg.objects.filter(password=password).exists():
                if (user_reg.objects.filter(email=name).exists()):
                    se=user_reg.objects.get(email=name)
                    request.session['userid']=se.id
                    return display_User(request)
                if name.isnumeric()==True:
                    if (user_reg.objects.filter(phone_number=name).exists()):
                        se=user_reg.objects.get(phone_number=name)
                        request.session['userid']=se.id
                        return display_User(request)
                    else:
                        return render(request,"User/login.html",{"form":form,"form1":form1,"msg7":'invalid data'})
                else:
                    return render(request,"User/login.html",{"form":form,"form1":form1,"msg7":'invalid data'})
                
            else:
                return render(request,"User/login.html",{"form":form,"form1":form1,"msg8":'pasword invalid'})
        else:
            print("not valid")
    return render(request,"User/login.html",{"form":form,"form1":form1})


def logout(request):
    request.session.clear()    
    request.session.flush()
    return render(request,"User/home.html")


#Display of staff home page
def display_User(request):
    cart = request.session.get('userid')
    emp=user_reg.objects.filter(id=cart)
    return render(request,"User/user_home.html",{"form":emp})

#Display of staff profile edit page
def display_edit(request):
    cart = request.session.get('userid')
    emp=user_reg.objects.filter(id=cart)
    return render(request,"User/user_edit.html",{"form":emp})

#Update staff detail
def upadte_user(request):
    cart = request.session.get('userid')
    emp=user_reg.objects.filter(id=cart)
    fname=request.POST['first_name']
    lname=request.POST['last_name']
    email=request.POST['email']
    pnumber=request.POST['phone_number']
    if fname=="" or lname=="" or email=="" or pnumber=="":
        return render(request,"User/user_edit.html",{"form":emp,'msg':"A field is empty"})
    else:
        emp.update(first_name=fname,last_name=lname,email=email,phone_number=pnumber)
        return display_User(request)

#display product details 
def display_product(request):
    form2=productForm   
    emp=product_details.objects.all()
    return render(request,"Product/product_add.html",{"form2":form2,'form3':emp})

#add product details 
def addproduct(request):
    form2=productForm
    emp=product_details.objects.all()
    if request.method=='POST':
        form2=productForm(request.POST)
        if form2.is_valid():
            pname=request.POST['product_name']
            if product_details.objects.filter(product_name=pname).exists():
                return render(request,"Product/product_add.html",{"form2":form2,'form3':emp,'msg1':'Product already added'})
            else:
                form2.save()
                return render(request,"Product/product_add.html",{"form2":form2,'form3':emp,'msg5':'Product added'})
    return render(request,"Product/product_add.html",{"form2":form2,'form3':emp})

#search product details 
def searchproduct(request):
    if request.method=='POST':
        pname=request.POST['selectproduct']
        emp1=product_details.objects.filter(product_name=pname)
        form2=productForm   
        emp=product_details.objects.all()
        return render(request,"Product/product_add.html",{"form2":form2,'form3':emp,'form4':emp1})

#update product details 
def updateproduct(request):
    form2=productForm   
    emp=product_details.objects.all()
    if request.method=='POST':
        pname=request.POST['prname']
        prate=request.POST['prate']
        pstat=request.POST['pstatus']
        pdiscrip=request.POST['pspec']
        if pstat!="Select status":
            emp2=product_details.objects.filter(product_name=pname)
            emp2.update(product_rate=prate,product_status=pstat,product_description=pdiscrip)
            return render(request,"Product/product_add.html",{"form2":form2,'form3':emp})











