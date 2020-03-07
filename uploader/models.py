from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class FileUploadCounter(SingletonModel):
    count = models.PositiveIntegerField("Counter", default=0)

    def __str__(self):
        return str(self.count)

    def save(self, *args, **kwargs):

        return super(FileUploadCounter, self).save(*args, **kwargs)


FileUploadCounter.load()
