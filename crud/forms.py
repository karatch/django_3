from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    age = forms.IntegerField(label='Ваш возраст')
