import io

from django.conf import settings
from django.views.generic import TemplateView
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from rest_framework import views
from rest_framework.response import Response

from drive_connect.serializers import GooglePhotosUploadInputSerializer


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        context["developer_key"] = settings.GOOGLE_API_DEV_KEY
        context["client_id"] = settings.GOOGLE_CLIENT_ID
        context["google_app_id"] = settings.GOOGLE_APP_ID
        return context


class FileUploadViewSet(views.APIView):
    def get_google_drive_service(self, access_token):
        credentials = Credentials(token=access_token)
        service = build("drive", "v3", credentials=credentials)
        return service

    def post(self, request, format=None, *args, **kwargs):
        serializer = GooglePhotosUploadInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        file_list = validated_data.get("fileList", None)
        drive_service = self.get_google_drive_service(
            access_token=validated_data.get("token", None)
        )
        for file_id in file_list:
            # Try to download the file
            request = drive_service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            # fh = io.FileIO(file_id + ".jpg", "wb") for local download

            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d%%." % int(status.progress() * 100))

        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
