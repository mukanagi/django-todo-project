from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import ToDoItem
from .forms import ToDoItemCreateForm


class ToDoIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:3]


class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm


# Кастомное поведение
# def get_success_url(self):
#     return reverse(
#         viewname="todo_list:detail",
#         kwargs={"pk": self.object.pk},
#         )
