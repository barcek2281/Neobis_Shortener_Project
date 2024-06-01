from django.db import models
from django.core.validators import URLValidator
from rest_framework.exceptions import ValidationError


class Url(models.Model):
    link = models.CharField(max_length=10_000)
    uuid = models.CharField(max_length=10)

    def is_valid(self) -> bool:
        try:
            URLValidator()(self.link)
            return True
        except :
            return False
