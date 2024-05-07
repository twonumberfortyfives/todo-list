from django.urls import path

from website.views import (
    task_status_switch,
    TaskCreateView,
    TaskListView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path("tasks/<int:pk>/switch/", task_status_switch, name='task-status-switch'),
    path("tags/", TagListView.as_view(), name='tag-list'),
    path("tags/create/", TagCreateView.as_view(), name='tag-create'),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = 'website'
