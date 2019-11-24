from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

MAX_STRLEN = 85 # default max length for char fields
MAX_TXTLEN = 2000 # default max length for text fields


class DepTour(models.Model):
    """
    Model for a department tour
    """

    class Meta:
        verbose_name = "Department Tours"

    name            = models.CharField(max_length=MAX_STRLEN, default='', verbose_name="title")
    email           = models.CharField(max_length=MAX_STRLEN, default='')
    confirm_email   = models.CharField(max_length=MAX_STRLEN, default='')
    desired_date    = models.DateTimeField(auto_now_add=True)
    phone           = models.CharField(max_length=10, default='')
    comments        = models.TextField(max_length=MAX_TXTLEN, blank=True, default='')

    # whether officer reviewed this request
    reviewed        = models.BooleanField(default=False)
    # whether officer confirmed this request
    # if reviewed == True and confirmed == False, then officer declined request
    # if reviewed == False, then challenge is not confirmed no matter what the field confirmed equals
    confirmed       = models.BooleanField(default=False)
    request_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
