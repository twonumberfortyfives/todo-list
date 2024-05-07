from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.http import require_http_methods

from website.forms import TaskCreationForm
from website.models import Task, Tags


def index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="home.html")


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("website:task-list")


class TaskListView(generic.ListView):
    model = Task
    template_name = "home.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context["task_amount"] = Task.objects.all().count()
        return context


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("website:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_delete_confirm.html"
    success_url = reverse_lazy("website:task-list")


@require_http_methods(["GET", "POST"])
def task_status_switch(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        if task.status:
            task.status = False
        else:
            task.status = True
        task.save()
        return redirect(
            "website:task-list"
        )  # Redirect to the home page after toggling status

    # Handle GET request
    return redirect("website:task-list")


class TagListView(generic.ListView):
    model = Tags
    template_name = "tags_list.html"
    context_object_name = "tag_list"


class TagCreateView(generic.CreateView):
    model = Tags
    template_name = "tags_form.html"
    fields = "__all__"
    success_url = reverse_lazy("website:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tags
    template_name = "tags_form.html"
    fields = "__all__"
    success_url = reverse_lazy("website:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tags
    template_name = "tag_delete_confirm.html"
    success_url = reverse_lazy("website:tag-list")
