from django.shortcuts import render
from .models import ToDo


def index(request):
    todos = ToDo.objects.all()
    return render(
        request,
        "todo_project/index.html",
        {"todo_list": todos, "title": "Главная Страница"},
    )
