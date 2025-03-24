from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser

# class NoteList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer