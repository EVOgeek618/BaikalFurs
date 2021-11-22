from django.shortcuts import render, redirect
from .forms import Search, Back, Add_Forum_Theme, Commeent
from .models import Photo, Ask, Otchets, URL_Video, Forum_Topic, Comment
import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.mail import send_mail, BadHeaderError
import time
def home(request):
    search = Search()
    list_theme={'1':"Продажа товара", '2': "Сотрудничество", '3':"Охота и лесное хозяйство", '4':'Прочее'}
    que = Back()
    lis = list(Otchets.objects.order_by("-date", "name").all())[:3]
    phs = []
    for i in lis:
        phs.append([i, list(Photo.objects.filter(otchet=i, is_video=False))[0].dir_way])
    if request.method == 'POST':
        ret = Back(request.POST)
        if ret.is_valid():
            theme = list_theme[ret.cleaned_data['theme']]
            email = ret.cleaned_data['email']
            quetion = ret.cleaned_data['quetion']
            Ask.objects.create(name=theme, email=email, quetion=quetion, date=datetime.datetime.now())
            try:
                pass
                #send_mail(f'{theme} от {email}', quetion,["stevenorton2610@gmail.com"], ["stevenorton2610@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            que = None
    return render(request,"home.html", context={"form_search":search,"form_q":que,"lis":phs})

def faq(request):
    search = Search()
    list_theme = {'1': "Продажа товара", '2': "Сотрудничество", '3': "Охота и лесное хозяйство", '4':'Прочее'}
    que = Back()
    if request.method == 'POST':
        ret = Back(request.POST)
        if ret.is_valid():
            theme = list_theme[ret.cleaned_data['theme']]
            email = ret.cleaned_data['email']
            user = ret.cleaned_data['name']
            quetion = ret.cleaned_data['quetion']
            Ask.objects.create(name=theme, user=user, email=email, quetion=quetion, date=datetime.datetime.now())
            try:
                que = None
                #send_mail(f'{theme} от {email}', quetion,["stevenorton2610@gmail.com"], ["stevenorton2610@gmail.com"])
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
    return render(request, "FAQ.html", context={"form_search": search,"form_q":que})

def forum(request,theme=None):
    search = Search()
    list_theme = {"1": "Продукция охоты – предложения, качество, объёмы, цены",
                  "2": "Охота, охотничьи путешествия, трофеи",
                  "3": "Способы и орудия охоты",
                  "4": "Актуальные правовые и организационно-экономические проблемы охотничьего хозяйства",
                  "5": "Иркутский охотфак – поиск и общение сокурсников, выпускников, педагогов"}
    topic = Forum_Topic.objects.order_by("-start_data").all()
    if theme in list_theme.keys():
        topic = Forum_Topic.objects.filter(theme=list_theme[theme]).all()
        return render(request, "forum.html", context={"form_search": search, "topics": topic, "theme":theme})
    elif not theme:
        return render(request, "forum.html", context={"form_search": search, "topics": topic})
    else:
        return redirect(f"/forum")

def contacts(request):
    search = Search()
    return render(request, "contacts.html", context={"form_search": search})

def photo(request):
    search = Search()
    lis = list(Otchets.objects.order_by("-date","name").all())
    phs=[]
    for i in lis:
        phs.append([i,list(Photo.objects.filter(otchet=i,is_video=False))[0].dir_way])
    phs.extend([[None] for i in range(5-len(phs)%5)])
    print(phs)
    phs_s = []
    for i in range(0, len(phs), 5):
        phs_s.append(phs[i:i + 5])
    return render(request, "Photo_Video.html", context={"form_search": search, "columns": phs_s})

def otchet(request, name):
    search = Search()
    phs = list(Photo.objects.filter(otchet=Otchets.objects.get(id=name)))
    urlvideos = list(URL_Video.objects.filter(otchet=Otchets.objects.get(id=name)))
    photos = []
    videos = []
    for i in phs:
        if i.is_video:
            videos.append(i.dir_way)
        else:
            photos.append(i.dir_way)
    return render(request, "otchets.html", context={"form_search": search, "photos": photos, "videos": videos,
                                                    "title":Otchets.objects.get(id=name).name, "text":Otchets.objects.get(id=name).text,
                                                    "urlvideos":urlvideos})

def products(request):
    search = Search()
    return render(request, "products.html", context={"form_search": search})

def add_forum_theme(request,stheme=1):
    add = Add_Forum_Theme()
    add.fields['theme'].initial = stheme
    search = Search()
    if request.method == 'POST':
        add = Add_Forum_Theme(request.POST)
        list_theme = {"1": "Продукция охоты – предложения, качество, объёмы, цены",
                     "2": "Охота, охотничьи путешествия, трофеи",
                     "3": "Способы и орудия охоты",
                     "4": "Актуальные правовые и организационно-экономические проблемы охотничьего хозяйства",
                     "5": "Иркутский охотфак – поиск и общение сокурсников, выпускников, педагогов"}
        if add.is_valid():
            theme = list_theme[add.cleaned_data['theme']]
            title = add.cleaned_data['title']
            user = add.cleaned_data['name']
            quetion = add.cleaned_data['quetion']
            new_id = Forum_Topic.objects.create(title=title, user=user, theme=theme, start_data=datetime.datetime.now(), text=quetion).id
            return redirect(f"/forum/{new_id}")
    return render(request, "add_forum_theme.html", context={"form": add, "form_search": search})
def topic(request, id):
    try:
        topic = Forum_Topic.objects.get(id=id)
        search = Search()
        com = Commeent()
        list_theme = {"Продукция охоты – предложения, качество, объёмы, цены": "1",
                      "Охота, охотничьи путешествия, трофеи":"2",
                      "Способы и орудия охоты": "3",
                      "Актуальные правовые и организационно-экономические проблемы охотничьего хозяйства": "4",
                      "Иркутский охотфак – поиск и общение сокурсников, выпускников, педагогов": "5"}
        if request.method == 'POST':
            com = Commeent(request.POST)
            if com.is_valid():
                text = com.cleaned_data['text']
                parent = com.cleaned_data['parent']
                name = com.cleaned_data['name']
                new_id = Comment.objects.create(topic=topic, data=datetime.datetime.now(), text=text,
                                                quetion=parent if parent>0 else None, user=name).id
                return redirect(f"/forum/{id}#{new_id}")
        comments = list(Comment.objects.filter(topic=topic))
        for i,el in enumerate(comments):
            if el.quetion:
                comments[i]=[el,Comment.objects.get(id=el.quetion)]
            else:
                comments[i] = [el]
        return render(request, "topic.html", context={"topic": topic, "form_search": search, "form_comment": com, \
                                                      "comments":comments, "theme": list_theme[topic.theme]})
    except:
        return HttpResponseNotFound()