from django.contrib import admin
from .models import DepTour

class ToursAdmin(admin.ModelAdmin):

    fields = ['name', 'confirmed', 'date', 'desired_time', 'email', 'phone', \
    	'comments', 'deprel_comments']
    	
    list_display = ('name','confirmed', 'email', 'date', 'desired_time', \
    	'date_submitted', 'phone', 'comments', 'deprel_comments')

admin.site.register(DepTour,ToursAdmin)
