from django.urls import path
from notes.views import NotesRUDView, NotesLCView

urlpatterns = [
    path("notes/<int:pk>", NotesRUDView.as_view(), name="notes_read_update_delete"),
    path("notes/", NotesLCView.as_view(), name="notes_list_create"),
]
