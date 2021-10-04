from django.shortcuts import render
from .forms import Search, Back
def home(request):
    search = Search()
    que = Back()
    return render(request,"home.html", context={"form_search":search,"form_q":que})

def faq(request):
    search = Search()
    que = Back()
    return render(request, "FAQ.html", context={"form_search": search,"form_q":que})

def forum(request):
    search = Search()
    return render(request, "forum.html", context={"form_search": search})

def contacts(request):
    search = Search()
    return render(request, "contacts.html", context={"form_search": search})

def photo(request):
    search = Search()
    return render(request, "Photo_Video.html", context={"form_search": search})

def products(request):
    search = Search()
    return render(request, "products.html", context={"form_search": search})
