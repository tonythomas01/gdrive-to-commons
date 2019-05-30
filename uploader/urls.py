from django.conf.urls import url

from uploader.views import FileUploadViewSet


urlpatterns = [url(r"", FileUploadViewSet.as_view(), name="file_upload")]
