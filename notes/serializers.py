from rest_framework.serializers import ModelSerializer
from notes.models import NotesModel


class NotesSerializer(ModelSerializer):
    class Meta:
        model = NotesModel
        fields = "__all__"
        read_only_fields = ("created_at", "modified_at", "is_active")
        write_only_fields = ("title", "description")
