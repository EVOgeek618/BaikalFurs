from django.shortcuts import render
from .forms import Search, Back
def home(request):
    search = Search()
    que = Back()
    return render(request,"home.html", context={"form_search":search,"form_q":que})
def faq(request):
    search = Search()
    return render(request, "FAQ.html", context={"form_search": search})
# Create your views here.
