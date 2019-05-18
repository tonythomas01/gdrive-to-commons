from rest_framework import serializers, fields


class FileSerializer(serializers.Serializer):
    name = fields.CharField(allow_blank=True)
    id = fields.CharField(allow_blank=True)


class GooglePhotosUploadInputSerializer(serializers.Serializer):
    fileList = FileSerializer(many=True)
    token = fields.CharField()
