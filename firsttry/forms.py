from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Search(forms.Form):
    text = forms.CharField(max_length=40, min_length=6)

class Back(forms.Form):
    theme = forms.ChoiceField(choices=((1, "Продажа товара"),
                                       (2, "Сотрудничество"),
                                       (3, "Охота и охотьничье хозяйство"),
                                       (4,"Прочее")),
                                        label="Тема вопросов:")
    name = forms.CharField(max_length=50, label="Ваше имя:", empty_value='', )
    email = forms.EmailField(label="Эл. почта:")
    quetion = forms.CharField(widget=forms.Textarea, label="Вопрос:")
class Back_not(forms.Form):
    theme = forms.ChoiceField(choices=((1, "Продажа товара"),
                                       (2, "Сотрудничество"),
                                       (3, "Охота и охотьничье хозяйство"),
                                       (4, "Прочее")),
                              label="Тема вопросов:")
    quetion = forms.CharField(widget=forms.Textarea, label="Вопрос:")
class Add_Forum_Theme(forms.Form):
    title = forms.CharField(max_length=50,label="Заголовок: ")
    theme = forms.ChoiceField(choices=((1, "Продукция охоты – предложения, качество, объёмы, цены"),
                                       (2, "Охота, охотничьи путешествия, трофеи"),
                                       (3, "Способы и орудия охоты"),
                                       (4,"Актуальные правовые и организационно-экономические проблемы охотничьего хозяйства"),
                                       (5, "Иркутский охотфак – поиск и общение сокурсников, выпускников, педагогов")),
                                        label="Тема форума:")
    quetion = forms.CharField(widget=forms.Textarea, label="Описание обсуждения: ")

class Commeent(forms.Form):
    parent = forms.IntegerField(initial=0)
    text = forms.CharField(widget=forms.Textarea)

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class SignIn(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")