from django.shortcuts import render, redirect
from .models import ToDo
from django.views.decorators.http import require_http_methods


def index(request):
    todos = ToDo.objects.all()
    return render(
        request,
        "todo_project/index.html",
        {"todo_list": todos, "title": "Главная Страница"},
    )


# указываем только одни метод запроса, при котором будет работаь наше предсталвление
@require_http_methods(["POST"])
def add(request):
    # берез значение поля title нашем модели ToDo
    title = request.POST["title"]
    # создаем новую запись в модели
    todo = ToDo(title=title)
    # сохраняем новосозданую запись
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.delete()
    return redirect("index")
