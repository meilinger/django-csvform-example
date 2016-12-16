from __future__ import unicode_literals
from django.db import models


class ModelWithCSV(models.Model):
    OPTIONS = ('http://example.com', 'http://example2.com', 'http://example3.com')

    csv_field = models.CharField(max_length=2000, blank=True, null=True)
