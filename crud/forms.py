from django import forms
from django.forms import SelectDateWidget


class UserForm(forms.Form):
    name = forms.CharField(label='Имя', initial='undefined', help_text='Введите свое имя')
    age = forms.IntegerField(
        label='Ваш возраст', initial=16, widget=forms.Textarea, help_text='Введите свой возраст'
    )
    field_order = ['age', 'name']
