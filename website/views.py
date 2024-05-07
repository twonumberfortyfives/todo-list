from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import generic

from website.models import Task


def index(request: HttpRequest) -> HttpResponse:
    return render(request, template_name="home.html")


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "task_form.html"
    fields = "__all__"


class TaskListView(generic.ListView):
    model = Task
    template_name = "home.html"
