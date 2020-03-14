import io

from django.conf import settings
from django.views.generic import TemplateView
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from rest_framework import views, status
from rest_framework.response import Response

from uploader.serializers import GooglePhotosUploadInputSerializer
from uploader.wiki_uploader import WikiUploader

from uploader.models import FileUpload


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        count = 0
        for record in FileUpload.objects.all():
            count += record.number_of_files
        context["count"] = count
        return context


class UploadPageView(TemplateView):
    template_name = "upload.html"

    def get_context_data(self, **kwargs):
        context = super(UploadPageView, self).get_context_data()
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
        social_auth = self.request.user.social_auth.get(
            provider="mediawiki"
        ).extra_data["access_token"]
        wiki_uploader = WikiUploader(
            host=settings.WIKI_URL,
            consumer_secret=settings.SOCIAL_AUTH_MEDIAWIKI_SECRET,
            consumer_token=settings.SOCIAL_AUTH_MEDIAWIKI_KEY,
            access_token=social_auth.get("oauth_token", None),
            access_secret=social_auth.get("oauth_token_secret", None),
        )

        uploaded_results = []

        file_upload_log = FileUpload(username=request.user.username)

        count = 0
        for file in file_list:
            request = drive_service.files().get_media(fileId=file["id"])
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False

            while done is False:
                download_status, done = downloader.next_chunk()

            uploaded, image_info = wiki_uploader.upload_file(
                file_name=file["name"], file_stream=fh, description=file["description"]
            )
            if uploaded:
                uploaded_results.append(image_info)
                count += 1
        file_upload_log.number_of_files = count
        file_upload_log.save()

        return Response(data=uploaded_results, status=status.HTTP_200_OK)
