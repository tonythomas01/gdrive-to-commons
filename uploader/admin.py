from django.contrib import admin

from .models import FileUploadCounter

# Register your models here.
# admin.site.register(FileUploadCounter)
@admin.register(FileUploadCounter)
class FileUploadCounterAdmin(admin.ModelAdmin):
    pass
