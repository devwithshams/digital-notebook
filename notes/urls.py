from django.urls import path
from .views import NoteList, NoteDetail

urlpatterns = [
    path('', NoteList.as_view(), name='note-list'),
    path('<uuid:pk>/', NoteDetail.as_view(), name='note-detail'),
]