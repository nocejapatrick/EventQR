from django.db import models

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.EventName
    EventName = models.CharField(max_length=200)
    EventStarted = models.DateTimeField()
    EventEnded = models.DateTimeField()

class Day(models.Model):
    DayTitle = models.CharField(max_length=200)

class Attendee(models.Model):
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)

class EventAttendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=200)

class EventAttendeeDay(models.Model):
    event_attendee = models.ForeignKey(EventAttendee, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    datestamp = models.DateTimeField(null = True)