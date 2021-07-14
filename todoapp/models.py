from django.db import models


class Todo(models.Model):
    code = models.ForeignKey(
        'rooms.Code',
        on_delete=models.CASCADE,
        default=None

    )
    task = models.CharField(max_length=200, null=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
