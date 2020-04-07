import datetime
import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient ,force_authenticate
from rest_framework import status

from uploader.models import FileUpload
from uploader.serializers import GooglePhotosUploadInputSerializer

class FileUploadModelTest(TestCase):
    def setUp(self):
        self.obj = FileUpload.objects.create(
            number_of_files=10, username="test_username", uploaded_at=datetime.datetime.now())

    def test_initialization(self):
        self.assertEqual(self.obj.number_of_files,
                         FileUpload.objects.get().number_of_files)

    def test_count_up(self):

        obj = FileUpload.objects.get()
        obj.number_of_files += 5
        obj.save()
        self.assertEqual(obj.number_of_files,
                         FileUpload.objects.get().number_of_files)


