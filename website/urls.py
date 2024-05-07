from django.urls import path

from website.views import (
    task_status_switch,
    TaskCreateView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path("tasks/<int:pk>/switch/", task_status_switch, name='task-status-switch'),
]

app_name = 'website'
