from django import forms

class Search(forms.Form):
    Поиск = forms.CharField(max_length=40)

class Back(forms.Form):
    theme = forms.ChoiceField(choices=((1, "Продажа товара"),
                                       (2, "Сотрудничество"),
                                       (3, "Охота и лесное хозяйство")),
                                        label="Тема вопросов:")
    email = forms.EmailField(label="Эл. почта:")
    quetion = forms.CharField(widget=forms.Textarea, label="Вопрос:")

