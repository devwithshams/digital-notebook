from django.contrib import admin
from .models import Note, Collaborator, NoteFile, NoteHistory

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "updated_at", "is_public")
    list_filter = ("is_public", "created_at")
    search_fields = ("title", "user__username")
    ordering = ("-created_at",)

class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ("note", "user", "permission_level")
    list_filter = ("permission_level",)
    search_fields = ("note__title", "user__username")

class NoteFileAdmin(admin.ModelAdmin):
    list_display = ("note", "file", "uploaded_at")
    ordering = ("-uploaded_at",)

class NoteHistoryAdmin(admin.ModelAdmin):
    list_display = ("note", "user", "timestamp")
    ordering = ("-timestamp",)

admin.site.register(Note, NoteAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(NoteFile, NoteFileAdmin)
admin.site.register(NoteHistory, NoteHistoryAdmin)
