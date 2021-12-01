from django.shortcuts import render, redirect
from .forms import Search, Back, Add_Forum_Theme, Commeent, Registration, SignIn, Back_not
from .models import Photo, Ask, Otchets, URL_Video, Forum_Topic, Comment
from django.contrib.auth.models import User
import datetime
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from  django.core.exceptions import ObjectDoesNotExist
import random
S = []
S.extend(range(48,58))
S.extend(range(65, 91))
S.extend(range(97,123))
ls = [chr(i) for i in S]
def home(request):
    search = Search()
    list_theme={'1':"Продажа товара", '2': "Сотрудничество", '3':"Охота и лесное хозяйство", '4':'Прочее'}
    que = Back() if not request.user.is_authenticated else Back_not()
    lis = list(Otchets.objects.order_by("-date", "name").all())[:3]
    phs = []
    for i in lis:
        phs.append([i, list(Photo.objects.filter(otchet=i, is_video=False))[0].dir_way])
    if request.method == 'POST':
        ret = Back(request.POST) if not request.user.is_authenticated else Back_not(request.POST)
        if ret.is_valid():
            theme = list_theme[ret.cleaned_data['theme']]
            email = request.user.email if request.user.is_authenticated else ret.cleaned_data['email']
            user = request.user.username if request.user.is_authenticated else ret.cleaned_data['name']
            quetion = ret.cleaned_data['quetion']
            Ask.objects.create(name=theme, user=user, email=email, quetion=quetion, date=datetime.datetime.now())
            que = None
    return render(request,"home.html", context={"form_search":search,"form_q":que,"lis":phs})

def faq(request):
    search = Search()
    list_theme = {'1': "Продажа товара", '2': "Сотрудничество", '3': "Охота и лесное хозяйство", '4':'Прочее'}
    que = Back if not request.user.is_authenticated else Back_not()
    if request.method == 'POST':
        ret = Back(request.POST) if not request.user.is_authenticated else Back_not(request.POST)
        if ret.is_valid():
            theme = list_theme[ret.cleaned_data['theme']]
            email = request.user.email if request.user.is_authenticated else ret.cleaned_data['email']
            user = request.user.username if request.user.is_authenticated else ret.cleaned_data['name']
            quetion = ret.cleaned_data['quetion']
            Ask.objects.create(name=theme, user=user, email=email, quetion=quetion, date=datetime.datetime.now())
            que = None
    return render(request, "FAQ.html", context={"form_search": search,"form_q":que})

def forum(request,theme=None,text=None):
    search = Search()
    list_theme = {"1": "Продукция охоты – предложения, качество, объёмы, цены",
                  "2": "Охота, охотничьи путешествия, трофеи",
                  "3": "Способы и орудия охоты",
                  "4": "Актуальные правовые и организационно-экономические проблемы охотничьего хозяйства",
                  "5": "Иркутский охотфак – поиск и общение сокурсников, выпускников, педагогов"}
    topic = Forum_Topic.objects.order_by("-start_data").all()
    if request.method == 'POST':
        search = Search(request.POST)
        if search.is_valid():
            search = search.cleaned_data["text"]
            return redirect(f"/forum/search/{search}")
    if text:
        slist = Forum_Topic.objects.order_by("-start_data").all()
        topic = []
        for i in slist:
            if i.title.lower().find(text[:-2].lower()) != -1 \
                    or i.text.lower().find(text[:-2].lower()) != -1\
                    or i.theme.lower().find(text[:-2].lower()) != -1:
                topic.append(i)
        search['text'].initial = text
        return render(request, "forum.html", context={"form_search": search, "topics": topic, "themes": list_theme})
    if theme in list_theme.keys():
        topic = Forum_Topic.objects.filter(theme=list_theme[theme]).all()
        return render(request, "forum.html", context={"form_search": search,"theme":theme, "topics": topic,
                                                      "themes": list_theme})
    elif not theme:
        return render(request, "forum.html", context={"form_search": search, "topics": topic, "themes": list_theme})
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
    if not request.user.is_authenticated:
        return redirect('/forum')
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
    topic = Forum_Topic.objects.get(id=id)
    search = Search()
    list_theme = {"Продукция охоты – предложения, качество, объёмы, цены": "1",
                  "Охота, охотничьи путешествия, трофеи": "2",
                  "Способы и орудия охоты": "3",
                  "Актуальные правовые и организационно-экономические проблемы охотничьего хозяйства": "4",
                  "Иркутский охотфак – поиск и общение сокурсников, выпускников, педагогов": "5"}
    if request.user.is_authenticated:
        com = Commeent()
        if request.method == 'POST':
            com = Commeent(request.POST)
            if com.is_valid():
                text = com.cleaned_data['text']
                parent = com.cleaned_data['parent']
                name = request.user.username
                new_id = Comment.objects.create(topic=topic, data=datetime.datetime.now(), text=text,
                                                quetion=parent if parent>0 else None, user=name).id
                return redirect(f"/forum/{id}#{new_id}")
        comments = list(Comment.objects.filter(topic=topic))
        for i,el in enumerate(comments):
            if el.quetion:
                comments[i]=[el,Comment.objects.get(id=el.quetion)]
            else:
                comments[i] = [el]
    else:
        com = 'Необходима авторизация на сайте'
        comments = list(Comment.objects.filter(topic=topic))
        for i, el in enumerate(comments):
            if el.quetion:
                comments[i] = [el, Comment.objects.get(id=el.quetion)]
            else:
                comments[i] = [el]
    return render(request, "topic.html", context={"topic": topic, "form_search": search, "form_comment": com, \
                                                      "comments":comments, "theme": list_theme[topic.theme]})

def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    search = Search()
    form_r = Registration()
    if request.method == "POST":
        form_r = Registration(request.POST)
        if form_r.is_valid():
            global ls
            aut = ''.join(random.sample(ls,20))
            login = form_r.cleaned_data["username"]
            email = form_r.cleaned_data['email']
            password = form_r.cleaned_data['password1']
            send_mail("Подтверждение регистрации",
                      f'Для подтверждения регистрации на сайте компании OOO "Байкал-Фурс" перейдите по ссылке: \n'
                      f'https://muscus.herokuapp.com/activateuser/{aut}',
                      "stevenorton2610@gmail.com",
                      [f"{email}"])
            User.objects.create_user(email=email, username=login, password=password, is_staff=False, is_superuser=False,
                                is_active=False, last_name= aut)
            return redirect('/')
    return render(request, "registration.html", context={"form_search": search, "form_r":form_r})

def active(request, pas):
    try:
        w = User.objects.get(last_name=pas)
        w.last_name = ''
        w.is_active = True
        w.save()
        return HttpResponse("Регистрация успешно завершена <a href='/'>На главную</a>")
    except ObjectDoesNotExist:
        return redirect("/")
