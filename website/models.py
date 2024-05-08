from datetime import datetime

from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=500, blank=False)
    start_date = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tags", blank=True, related_name="tasks")

    class Meta:
        ordering = ["status"]


class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
