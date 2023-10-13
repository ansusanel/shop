from django.shortcuts import render,redirect
from.models import*
from UserApp.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def index(requset):
   return render(requset,'index.html')

def addcategories(request):   
   return render(request,'addcategories.html')

def viewcategories(request):
   data=Categorytable.objects.all()
   return render(request,'viewcategories.html',{'data':data})

def addproducts(request): 
   data=Categorytable.objects.all()  
   return render(request,'addproducts.html',{'data':data})

def viewproducts(request):
   data=Producttable.objects.all()
   return render(request,'viewproducts.html',{'data':data})

def registeredusers(request):
   data=Registrationtable.objects.all()
   return render(request,'registeredusers.html',{'data':data})

def feeback(request):
   data=Feedbacktable.objects.all()
   return render(request,'feeback.html',{'data':data})

def viewoders(request):
   data=Ordetable.objects.all()
   return render(request,'viewoders.html',{'data':data})

def categorydata(request):
   if request.method=='POST':
      name=request.POST['CategoryName']
      image=request.FILES['image']
      about=request.POST['CategoryDescription']
      data=Categorytable(CategoryName=name,image=image,CategoryDescrition=about)
      data.save()
      return redirect('viewcategories')
   
def editcategory(request):
    data=Categorytable.objects.all()
    return render(request,'viewcategory.html',{'data':data})

def editcat(request,id):
    data=Categorytable.objects.filter(id=id)
    return render(request,'editcategory.html',{'data':data})

def updatecategory(request,id):
    if request.method=='POST':
        name=request.POST['CategoryName']
        about=request.POST['CategoryDescription']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Categorytable.objects.get(id=id).image
        Categorytable.objects.filter(id=id).update(CategoryName=name,image=file,CategoryDescrition=about)
        return redirect('viewcategories')
    
def delete(request,id):
    Categorytable.objects.get(id=id).delete()
    return redirect('viewcategories')   
  

def productdata(request):
   if request.method=='POST':
      cname=request.POST['CategoryName']
      name=request.POST['ProductName']
      image=request.FILES['image']
      about=request.POST['ProductDescription']
      price=request.POST['ProductPrice']
      data=Producttable(CategoryName=cname,ProductName=name,image=image,ProductDescrition=about,ProductPrice=price)
      data.save()
      return redirect('viewproducts')

def editproduct(request):
    data=Producttable.objects.all()
    return render(request,'viewproducts.html',{'data':data})

def editprod(request,id):
    data=Producttable.objects.filter(id=id)
    return render(request,'editproducts.html',{'data':data})

def updateproduct(request,id):
    if request.method=='POST':
        cname=request.POST['CategoryName']
        pname=request.POST['ProductName']
        ProductDescrition=request.POST['ProductDescrition']
        ProductPrice=request.POST['ProductPrice']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Producttable.objects.get(id=id).image
        Producttable.objects.filter(id=id).update(CategoryName=cname,ProductName=pname,image=file,ProductDescrition=ProductDescrition,ProductPrice=ProductPrice)
        return redirect('viewproducts')
    
def deleteprod(request,id):
    Producttable.objects.get(id=id).delete()
    return redirect('viewproducts')  