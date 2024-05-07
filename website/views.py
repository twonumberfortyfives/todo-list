from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from website.forms import TaskCreationForm
from website.models import Task


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


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "task_form.html"
    form_class = TaskCreationForm
    success_url = reverse_lazy("website:task-list")
