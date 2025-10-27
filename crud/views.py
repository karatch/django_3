from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import UserForm


def index(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        last_name = request.POST.get('last_name')
        return HttpResponse(f'<h2>Привет, {name} {last_name}! Твой возраст: {age}</h2>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})