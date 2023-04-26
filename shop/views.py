from django.shortcuts import render ,redirect
from . models import *
from django.contrib import messages

# Create your views here.

def about(request):
    return render(request,"shop/about.html")
def collection(request):
    category = Category.objects.filter(status=0)
    return render(request,"shop/collection.html",{"Category":category})
def collectionview(request,name):
    if Category.objects.filter(name=name,status=0):
        products = Product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No such category")
        return redirect('collections')
def product_details(request,name,pname):
    if(Category.objects.filter(name=name,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Produtct Found")
        return redirect('collection')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collection')