from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
def products(request):
    return render(request,'products.html')
def faq(request):
    return render(request,'faq.html')
def contacts(request):
    return render(request,'contact.html')







