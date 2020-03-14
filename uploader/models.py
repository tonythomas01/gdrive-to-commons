from django.db import models

from django.utils import timezone


class FileUpload(models.Model):

    number_of_files = models.PositiveIntegerField("Number of Files Uploaded", default=0)
    username = models.CharField("Username", max_length=80)
    uploaded_at = models.DateTimeField("Uploaded at", auto_now=True, editable=False)

    def __str__(self):
        return "{0}:  {1} : {2})".format(
            self.username, str(self.number_of_files), str(self.uploaded_at)
        )
