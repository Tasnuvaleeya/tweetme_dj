from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_content

# Create your models here.



class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content =='abc':
    #         raise ValidationError("Content Can not be ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)