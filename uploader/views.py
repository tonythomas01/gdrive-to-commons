import io
import os

from django.conf import settings
from django.views.generic import TemplateView
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from rest_framework import views, status
from rest_framework.response import Response

from uploader.serializers import GooglePhotosUploadInputSerializer
from uploader.upload_helpers import upload_files_to_commons


class HomePageView(TemplateView):
    template_name = "home.html"

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
        social_auth = self.request.user.social_auth.get(provider="mediawiki")
        user_access_token = social_auth.extra_data["access_token"]

        # Use this user_access_token to upload to commons later.
        if not os.path.exists("tmp/"):
            os.mkdir("tmp")

        for file in file_list:
            request = drive_service.files().get_media(fileId=file["id"])
            file_ext = os.path.splitext(file["name"])[1]
            fh = io.FileIO("tmp/" + file["id"] + file_ext, "wb")

            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                download_status, done = downloader.next_chunk()
                print("Download %d%%." % int(download_status.progress() * 100))

        upload_files_to_commons(user_access_token)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)
