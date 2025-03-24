from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Note

class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )

        cls.note = Note.objects.create(
            user=cls.user,
            title="Test Note",
            content="This is a test note.",
        )


    def test_note_model(self):
        self.assertEqual(self.note.user.username, "testuser")
        self.assertEqual(self.note.title, "Test Note")
        self.assertEqual(self.note.content, "This is a test note.")
        self.assertEqual(str(self.note), "Test Note")
        

    def test_note_collaborator(self):
        collaborator = self.note.collaborators.create(
            user=self.user,
            permission_level="edit",
        )
        self.assertEqual(collaborator.permission_level, "edit")
        self.assertEqual(str(collaborator), "testuser - Test Note (edit)")

    def test_note_file(self):
        note_file = self.note.files.create(
            file="note_files/test.txt",
        )
        self.assertEqual(str(note_file), "File for Test Note")

    def test_note_history(self):
        note_history = self.note.history.create(
            user=self.user,
            changes="{}",
        )
        self.assertEqual(str(note_history), "History - Test Note")

    