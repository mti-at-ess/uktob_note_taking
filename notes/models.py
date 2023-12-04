from django.db import models
from common.models import BaseModel


class NotesModel(BaseModel):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    summary = models.CharField(max_length=200)

    objects = models.Manager()
