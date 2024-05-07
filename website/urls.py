from django.urls import path

from website.views import (
    index,
    TaskCreateView,
    TaskListView,
    TaskUpdateView,
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update', TaskUpdateView.as_view(), name='task-update')

]

app_name = 'website'
