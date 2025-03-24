from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]  # Users must be logged in
    serializer_class = NoteSerializer

    def get_queryset(self):
        """Only return notes created by the logged-in user."""
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Ensure the note is assigned to the current user automatically."""
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]  # Only admin users can manage users
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
