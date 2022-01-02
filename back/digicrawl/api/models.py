import django.utils.timezone
from django.db import models


class Api(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.price)
