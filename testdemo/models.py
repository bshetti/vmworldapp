from __future__ import unicode_literals

from django.db import models

class Mortgage(models.Model):
    name = models.CharField(max_length=100)
    amount = models.FloatField(default=0)

    def _str_(self):
        return self.name
