from django.urls import path

from website.views import (
    index,
    TaskCreateView,
    TaskListView,
)

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('create-task/', TaskCreateView.as_view(), name='task-create'),

]

app_name = 'website'
