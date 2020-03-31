from rest_framework import serializers, fields


class FileSerializer(serializers.Serializer):
    name = fields.CharField(allow_blank=True)
    id = fields.CharField(allow_blank=True)
    datecreated = serializers.DateField(format='', input_formats='')
    description = fields.CharField(max_length=200, allow_blank=True, allow_null=True)


class GooglePhotosUploadInputSerializer(serializers.Serializer):
    fileList = FileSerializer(many=True)
    token = fields.CharField()
