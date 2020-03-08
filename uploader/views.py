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
        print(file_list[0])
        drive_service = self.get_google_drive_service(
            access_token=validated_data.get("token", None)
        )
        social_auth = self.request.user.social_auth.get(
            provider="mediawiki"
        ).extra_data["access_token"]
        # social_auth='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NTg5MmVlMTljMTk0MTQ2NDVhZDM3MzM4OGVjOGRhNSIsImp0aSI6IjczYWM0MWJkOGQyOGY3ZTc5NWY4OWE3NmE2ZDExNjhhYzU0M2U3YzA4ZTliYWVlMWZkNmQyNmM0MjFhZjM1MmE2MWRjNjhhYWZiOWI4NjllIiwiaWF0IjoxNTgzNTgyNTk3LCJuYmYiOjE1ODM1ODI1OTcsImV4cCI6OTIyMzM3MTI2MTI4NzU4MjU5Nywic3ViIjoiNjE3MzA0MTEiLCJzY29wZXMiOlsiYmFzaWMiLCJ1cGxvYWRmaWxlIiwidXBsb2FkZWRpdG1vdmVmaWxlIl19.Szxfm_IlAL5ripo8JV2EtgA2PXpQbQkZM8sB9eDSnVd3ZmhlDhRYkB0uTAp_SmrAABe_Uel78sec8EfmaG_0DwRdORKvIb-4fpbQIwLQZXRA3CzCYvQjupEook6Lg1z7nG-OJ04bXtKbVWpy7YjYM0fSrlgczOWfwQXgvUiimLf24LmH_uAR9UIy8VNThvN0LDHulqvHDMzUNNdLoi1hBjbMgKtsxzaS4IRfngR3VKsW-PUKN3xrzrsYpYeAJTlgxIQiYpLOqPNDTwQkCmSDpuswT-XGm0t8OuigCPeaa3Iv45Y7rMs9cArhhJlWJf-mcCQGJGCXyMX1dzCQDmYzkzoJxhmh_4U6nidMsJoEzMLCVkf7BjBALPjP0YJELHze0h5NjUnJgtO1vBt52zTkHbGk-qlWXnQkxOFiUKBDww3_l_iOte0SLr4ktIXZFb2x2RGdkyVsqG6fMZ6w7l6SBfSHYpnR5mSnonskQNDXiDfT4AmeLPnjiOVbj3Uk2f9sqeOrdDxC4hObELZHNps8Z4l8jmn76kMCFvaWz2VboZz7IvM5IuItnQKmCrvTLn3QOuu-v9dlqEBxtw4YgXvf51qKVtHUqVuuEFXcf4by2yce7cA2tJhVn76WwyLHub1f0YD-fhvBJ6XWPOLGSVrANrs2X6o0eV3XKmAFRo4MV1U'
        wiki_uploader = WikiUploader(
            host=settings.WIKI_URL,
            consumer_secret=settings.SOCIAL_AUTH_MEDIAWIKI_SECRET,
            consumer_token=settings.SOCIAL_AUTH_MEDIAWIKI_KEY,
            access_token=social_auth.get("oauth_token", None),
            access_secret=social_auth.get("oauth_token_secret", None),
        )

        uploaded_results = []

        current_user = FileUpload(username=request.user.username)

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
        current_user.number_of_files = count
        current_user.save()

        return Response(data=uploaded_results, status=status.HTTP_200_OK)
