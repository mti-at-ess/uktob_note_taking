from django.db import models
import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now)
    modified_at = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=1)
