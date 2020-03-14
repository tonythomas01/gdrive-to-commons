from django.contrib import admin

from uploader.models import FileUpload


@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ("username", "number_of_files", "uploaded_at")
    readonly_fields = ("username", "number_of_files", "uploaded_at")
