from django.shortcuts import render
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from .permissions import IsAuthorOrReadOnly

class NoteList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer