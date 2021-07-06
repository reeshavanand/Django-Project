from django.shortcuts import render, HttpResponse

from . models import Contact

from django.contrib import messages

# Create your views here.

def play(request):
      return render(request,'play.html',{'name':'customer'})


def add(request):

      val1 = int(request.POST['num1'])
      val2 = int(request.POST['num2'])
      res = val1 + val2
      return render(request,"result.html",{'result':res})

def index(request):
      return render(request, 'index.html')

def contact(request):

      if request.method=='POST':
            name=request.POST.get('name')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            password=request.POST.get('password')
            contact = Contact(name=name,phone=phone,email=email,password=password)
            contact.save()
            messages.success(request, 'Your Contact Details have been updated!!')
      return render(request, 'contact.html')

def cart(request):
      return render(request, 'cart.html')

def about(request):
      return render(request, 'about.html')

