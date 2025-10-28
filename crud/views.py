from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data.get('name')
            return HttpResponse(f'<h2>Hello, {name}</h2>')
        else:
            return HttpResponse('<h2>Invalid data</h2>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})