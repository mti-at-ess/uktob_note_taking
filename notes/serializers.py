from rest_framework.serializers import ModelSerializer
from notes.models import NotesModel


class NotesSerializer(ModelSerializer):
    class Meta:
        model = NotesModel
        fields = ("id", "title", "description", "summary")
