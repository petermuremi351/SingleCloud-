from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "project", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("name", "email", "phone", "project", "message", "created_at")