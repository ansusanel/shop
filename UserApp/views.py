from django.shortcuts import render,redirect
from.models import*
from AdminApp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def userindex(requset):
   return render(requset,'userindex.html')

def register(request):
   return render(request,'register.html')

def cardview(request):
   data=Producttable.objects.all()
   return render(request,'cardview.html',{'data':data})

def order(request):
   return order(request,'order.html')

def login(request):
   return render(request,'login.html')

def contact(request):
   return render(request,'contact.html')


def onecardview(request,productid):
    data=Producttable.objects.filter(id=productid)
    return render(request,'onecardview.html',{'data':data})

def order(request,productid):
   data=Producttable.objects.filter(id=productid)
   return render(request,'order.html',{'data':data})

def orderdata(request):
   if request.method=='POST':
      ProductName=request.POST['ProductName']
      ProductPrice=request.POST['ProductPrice']
      Name=request.POST['name']
      Email=request.POST['email']
      Number=request.POST['number']
      data=Ordetable(ProductName=ProductName,ProductPrice=ProductPrice,Name=Name,Email=Email,Number=Number)
      data.save()
      return redirect('cardview')
   

def feedbackform(request):
    return render(request,'feedbackform.html')

def feedbackdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['message']        
        data=Feedbacktable(UserName=name,Email=email,Message=msg)
        data.save()
        return redirect('cardview')   


def Registrationdata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']        
        data=Registrationtable(UserName=name,Email=email,Password=password)
        data.save()
        return redirect('cardview')
    

def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Registrationtable.objects.filter(UserName=username,Password=password).exists():
           data = Registrationtable.objects.filter(UserName=username,Password=password).values('Email','id').first()
           request.session['email_u'] = data['Email'] 
           request.session['u_id'] = data['id']
           request.session['username_u'] = username
           request.session['password_u'] = password 
           return redirect('cardview')          
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')

def userlogout(request):  
    del request.session['email_u']  
    del request.session['u_id']    
    del request.session['username_u']
    del request.session['password_u']
    return redirect('cardview')  





