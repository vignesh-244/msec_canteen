from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Count
from . models import Product,Basket
from django.contrib import messages
from . forms import CustomerRegistrationForm,CustomerProfileForm
# Create your views here.
def home(request):
    return render(request,"app/home.html")
 
def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"app/category.html",locals())
    
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())    
    
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,"app/productdetail.html",locals())

class CustomerRegistrationView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',locals())
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"congratulations! User Register Successfully")
        else:
            messages.error(request,"Invaild Input Data")
        return render(request,"app/customerregistration.html",locals())
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html', locals())
    def post(self,request):
        return render(request, 'app/profile.html',locals())

def add_to_basket(reuqest):
    user=reuqest.user
    product_id=reuqest.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Basket(user=user,product=product).save()
    return redirect("/cart")

def show_basket(request):
    user=request.user
    basket=basket.objects.filter(user=user)
    return render(request,'app/addtobasket.html',locals())