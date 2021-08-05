# Django
from django.db import models

class Todo(models.Model):
    # Todo model for Postgresql
    task = models.CharField(max_length=255, unique=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        content = f'{self.task} | {self.created}'
        return content
