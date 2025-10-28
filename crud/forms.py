from django import forms
from django.forms import SelectDateWidget


class UserForm(forms.Form):
    name = forms.CharField(
        label='Имя', help_text='Введите свое имя', min_length=2, max_length=10
    )
    age = forms.IntegerField(
        label='Ваш возраст',
        help_text='Введите свой возраст',
        required = False,
        min_value=1,
        max_value=99
    )
    reklama = forms.BooleanField(label='Согласны получать рекламу?', required=False)
    field_order = ['name', 'age']
