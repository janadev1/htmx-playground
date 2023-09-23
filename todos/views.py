from django.http import HttpResponse, QueryDict
from django.template import loader
from django.views.decorators.http import require_http_methods

from .models import Todo


@require_http_methods(["GET"])
def home(request):
    todos = Todo.objects.all()
    template = loader.get_template("home.html")
    context = {"todos": todos}
    return HttpResponse(template.render(context, request))


@require_http_methods(["GET"])
def todo_list(request):
    todos = Todo.objects.all()

    if search := request.GET.get("search"):
        todos = todos.filter(text__icontains=search)

    context = {"todos": todos}
    template = loader.get_template("todo_list.html")

    return HttpResponse(template.render(context, request))


@require_http_methods(["POST"])
def todo_add(request, *args, **kwargs):
    todo = Todo.objects.create(text=request.POST.get("text"))

    context = {"todo": todo}
    template = loader.get_template("todo_item.html")

    return HttpResponse(template.render(context, request))


@require_http_methods(["GET", "PUT"])
def todo_edit(request, *args, **kwargs):
    if request.method == "GET":
        id = kwargs["todo_id"]

        context = {"todo": Todo.objects.get(id=id)}
        template = loader.get_template("todo_edit.html")

        return HttpResponse(template.render(context, request))

    if request.method == "PUT":
        id = kwargs["todo_id"]
        todo = Todo.objects.get(id=id)

        data = QueryDict(request.body)

        todo.text = data.get("todo", todo.text)
        todo.save()

        context = {"todo": todo}
        template = loader.get_template("todo_item.html")

        return HttpResponse(template.render(context, request))


@require_http_methods(["DELETE"])
def todo_delete(request, *args, **kwargs):
    id = kwargs["todo_id"]
    Todo.objects.filter(id=id).delete()

    return HttpResponse()
