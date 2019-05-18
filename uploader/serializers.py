from rest_framework import serializers, fields


class FileListSerializer(serializers.Serializer):
    name = fields.CharField(allow_blank=True)
    id = fields.CharField(allow_blank=True)


class GooglePhotosUploadInputSerializer(serializers.Serializer):
    fileList = FileListSerializer()
    token = fields.CharField()
