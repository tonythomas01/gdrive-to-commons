from rest_framework import serializers, fields


class FileListField(fields.ListField):
    fileName = fields.CharField(allow_blank=True)
    fileId = fields.CharField(allow_blank=True)


class GooglePhotosUploadInputSerializer(serializers.Serializer):
    fileList = FileListField()
    token = fields.CharField()
