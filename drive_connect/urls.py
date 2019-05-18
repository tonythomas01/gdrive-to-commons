from django.conf.urls import url

from drive_connect.views import FileUploadViewSet

urlpatterns = [url(r"", FileUploadViewSet.as_view(), name="file_upload")]
