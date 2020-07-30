from django.contrib.sites.models import Site
from django.db import models


class UrlModel(models.Model):

    slug = models.SlugField(max_length=6, unique=True)
    url = models.URLField(max_length=500, unique=True)

    def get_absolute_url(self):
        return '{}/{}'.format(Site.objects.get_current().domain, self.slug)
