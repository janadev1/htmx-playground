from django.urls import path

from .views import home, todo_add, todo_delete, todo_edit, todo_list

urlpatterns = [
    path("", home),
    path("todos/", todo_list, name="todos"),
    path("todos/add/", todo_add, name="todo-add"),
    path("todos/<int:todo_id>/edit/", todo_edit, name="todo-edit"),
    path("todos/<int:todo_id>/delete/", todo_delete, name="todo-delete"),
]
