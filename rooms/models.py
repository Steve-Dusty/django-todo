from django.db import models
from todoapp.models import Todo


class Code(models.Model):
    room_code = models.CharField(max_length=64)

    def __str__(self):
        return self.room_code
