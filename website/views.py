from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic, View
from django.views.decorators.csrf import csrf_exempt
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


@method_decorator(csrf_exempt, name='post')
class TaskUpdateStatusView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        return redirect("website:task-list")

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.status = not task.status  # Toggle the status
        task.save()
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
