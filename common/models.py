from django.db import models
import datetime


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(default=datetime.datetime.now)
    modified_at = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=0)
