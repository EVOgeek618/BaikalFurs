from django import forms

class Search(forms.Form):
    Поиск = forms.CharField(max_length=40)

class Back(forms.Form):
    theme = forms.ChoiceField(choices=((1, "Продажа товара"),
                                       (2, "Сотрудничество"),
                                       (3, "Охота и охотьничье хозяйство"),
                                       (4,"Прочее")),
                                        label="Тема вопросов:")
    email = forms.EmailField(label="Эл. почта:")
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


