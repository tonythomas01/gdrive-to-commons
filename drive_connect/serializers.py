from rest_framework import serializers, fields


class FileListField(fields.ListField):
    fileId = fields.CharField(allow_blank=True)


class GooglePhotosUploadInputSerializer(serializers.Serializer):
    fileList = FileListField()
    token = fields.CharField()
