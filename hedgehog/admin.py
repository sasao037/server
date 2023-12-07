from django.contrib import admin
from .models import People
from .models import Event

# Register your models here.

class PeopleAdmin(admin.ModelAdmin):
  pass

admin.site.register(People, PeopleAdmin)

class EventAdmin(admin.ModelAdmin):
  pass

admin.site.register(Event, EventAdmin)
