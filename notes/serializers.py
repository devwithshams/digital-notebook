from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'is_public')
        read_only_fields = ('id', 'created_at', 'updated_at', 'user')  # Make user read-only

    def create(self, validated_data):
        """Assign the note to the logged-in user automatically."""
        request = self.context['request']
        validated_data['user'] = request.user
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
