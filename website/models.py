from datetime import datetime

from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=500)
    start_date = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField()
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tags", blank=True, related_name="tasks")


class Tags(models.Model):
    name = models.CharField(max_length=255)
