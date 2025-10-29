from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserForm


def index(request):
    userform = UserForm(request.POST or None)
    if request.method == 'POST':
        if userform.is_valid():
            name = userform.cleaned_data.get('name')
            return HttpResponse(f'<h3>Hello, {name}</h3>')
    return render(request, 'index.html', {'form': userform})
