from django.db import models
from users.models import CustomUser
import uuid

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=200)
    content = models.TextField()  # Supports rich text (Quill.js)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Collaborator(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="collaborators")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="shared_notes")
    PERMISSION_CHOICES = [
        ("view", "View Only"),
        ("edit", "Edit"),
    ]
    permission_level = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

    class Meta:
        unique_together = ("note", "user")

    def __str__(self):
        return f"{self.user} - {self.note.title} ({self.permission_level})"

class NoteFile(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="note_files/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for {self.note.title}"

class NoteHistory(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="history")
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    changes = models.TextField()  # JSON storing versioned changes
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History - {self.note.title}"
