from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom form for user creation (fixing usable_password issue)."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')  # Explicit fields

class CustomUserChangeForm(UserChangeForm):
    """Custom form for updating user details."""

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
