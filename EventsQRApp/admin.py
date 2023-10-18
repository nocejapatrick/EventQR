from django.contrib import admin
from .models import Event, Attendee, EventAttendee, EventAttendeeDay
# Register your models here.
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(EventAttendee)
admin.site.register(EventAttendeeDay)