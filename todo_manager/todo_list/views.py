from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from .models import ToDoItem
from .forms import (
    ToDoItemCreateForm,
    ToDoItemUpdateForm,
)


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


class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = "_update_form"
    form_class = ToDoItemUpdateForm


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem

    success_url = reverse_lazy("todo_list:list")


# Кастомное поведение пишется для каждого класса
# def get_success_url(self):
#     return reverse(
#         viewname="todo_list:detail",
#         kwargs={"pk": self.object.pk},
#         )
