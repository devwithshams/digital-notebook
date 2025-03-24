from django.db import router
# from django.urls import path
# from .views import NoteList, NoteDetail, UserList, UserDetail
from rest_framework.routers import SimpleRouter

from .views import NoteViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', NoteViewSet, basename='notes')

urlpatterns = router.urls

# urlpatterns = [
#     path('', NoteList.as_view(), name='note-list'),
#     path('<uuid:pk>/', NoteDetail.as_view(), name='note-detail'),
#     path('users/', UserList.as_view()),
#     path('users/<uuid:pk>/', UserDetail.as_view()),

# ]