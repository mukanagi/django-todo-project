from django.views.generic import (
    ListView,
    DetailView,
)
from .models import ToDoItem


class ToDoIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:3]


class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()

class ToDoDetailView(DetailView):
    model = ToDoItem