from django import forms
from django.forms import SelectDateWidget


class UserForm(forms.Form):
    name = forms.CharField(max_length=12, label='Имя', initial='John', help_text='Введите Ваше имя')
    last_name = forms.CharField(label='Фамилия', initial='Doe')
    age = forms.IntegerField(label='Ваш возраст', initial=18)
    married = forms.BooleanField(initial=False, required=False)
    date = forms.DateField(widget=SelectDateWidget)
