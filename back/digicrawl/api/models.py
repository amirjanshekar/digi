from django.db import models
from datetime import *


class Api(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.price)
