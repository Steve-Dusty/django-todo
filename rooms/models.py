from django.db import models
from todoapp.models import Todo


class Code(models.Model):
    todo = models.OneToOneField(
        'todoapp.Todo',
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
    )
    room_code = models.CharField(max_length=10)

    def __str__(self):
        return self.room_code
