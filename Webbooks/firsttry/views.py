from django.shortcuts import render, redirect
from .forms import Search, Back
from .models import Photo
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
def home(request):
    search = Search()
    list_theme={'1':"Продажа товара", '2': "Сотрудничество", '3':"Охота и лесное хозяйство"}
    que = Back()
    if request.method == 'POST':
        ret = Back(request.POST)
        if ret.is_valid():
            theme = list_theme[ret.cleaned_data['theme']]
            email = ret.cleaned_data['email']
            quetion = ret.cleaned_data['quetion']
            try:
                send_mail(f'{theme} от {email}', quetion,
                          ["stevenorton2610@gmail.com"], ["stevenorton2610@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('forum')
    else:
        return render(request,"home.html", context={"form_search":search,"form_q":que})

def faq(request):
    search = Search()
    list_theme = {'1': "Продажа товара", '2': "Сотрудничество", '3': "Охота и лесное хозяйство"}
    que = Back()
    if request.method == 'POST':
        ret = Back(request.POST)
        if ret.is_valid():
            theme = list_theme[ret.cleaned_data['theme']]
            email = ret.cleaned_data['email']
            quetion = ret.cleaned_data['quetion']
            try:
                send_mail(f'{theme} от {email}', quetion,
                          ["stevenorton2610@gmail.com"], ["stevenorton2610@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('forum')
    else:
        return render(request, "FAQ.html", context={"form_search": search,"form_q":que})

def forum(request):
    search = Search()
    return render(request, "forum.html", context={"form_search": search})

def contacts(request):
    search = Search()
    return render(request, "contacts.html", context={"form_search": search})

def photo(request):
    search = Search()
    phs = list(Photo.objects.filter(date="2021-10-20"))
    photos = []
    videos=[]
    for i in phs:
        if str(i.dir_way)[::-1][:str(i.dir_way)[::-1].find(".")][::-1] in ["mp4", "avi", "wav", "mkv"]:
            videos.append(i.dir_way)
        else:
            photos.append(i.dir_way)
    return render(request, "Photo_Video.html", context={"form_search": search, "photos": photos,"videos": videos})

def products(request):
    search = Search()
    return render(request, "products.html", context={"form_search": search})
