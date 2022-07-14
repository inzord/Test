from django.db import models
from hashlib import md5


class Url(models.Model):
    full_url = models.CharField(unique=True, max_length=200)
    short_url = models.CharField(unique=True, max_length=15)

    def __str__(self):
        return self.full_url

    @classmethod
    def create(self, full_url):
        temp_url = md5(full_url.encode()).hexdigest()[:5]
        try:
            obj = self.objects.create(full_url=full_url, short_url=temp_url)
        except:
            obj = self.objects.get(full_url=full_url)
        return obj
