from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django import forms

MAX_STRLEN = 255 # default max length for char fields
MAX_TXTLEN = 2000 # default max length for text fields

#.save adds to database
# POST user submits
#GET user wants something
class DepTour(models.Model):
    """
    Model for a department tour
    """

    class Meta:
        verbose_name = "Department Tour"

    name            = models.CharField(max_length=MAX_STRLEN, default='')
    email           = models.EmailField(max_length=MAX_STRLEN, default='')
    # verify_email    = models.EmailField(max_length=MAX_STRLEN, default='')
    desired_date    = models.DateTimeField()
    phone           = models.CharField(max_length=12, default='')
    comments        = models.TextField(max_length=MAX_TXTLEN, blank=True, default='', verbose_name='Additional comments')
    confirmed        = models.BooleanField(default=False)

    # whether officer reviewed this request
    # reviewed        = models.BooleanField(default=False)
    # confirmed       = models.BooleanField(default=False)
    # request_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
