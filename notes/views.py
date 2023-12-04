from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)

from notes.models import NotesModel
from notes.serializers import NotesSerializer


class NotesRUDView(RetrieveUpdateDestroyAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer


class NotesLCView(ListCreateAPIView):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer
