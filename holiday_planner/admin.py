from django.contrib import admin
from .models import Trip, Location

admin.site.register([Trip, Location])
