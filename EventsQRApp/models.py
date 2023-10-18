from django.db import models

# Create your models here.
class Event(models.Model):
    def __str__(self):
        return self.EventName
    EventName = models.CharField(max_length=200)
    EventStarted = models.DateTimeField()
    EventEnded = models.DateTimeField()

class Attendee(models.Model):
    def __str__(self):
        return u"(%i) %s %s %s" % (self.id, self.FirstName, self.MiddleName, self.LastName)
    
    @property
    def getFullName(self):
        return "%s %s %s" %(self.FirstName, self.MiddleName, self.LastName)
    
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)

class EventAttendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
    qrcode = models.CharField(max_length=200)

class EventAttendeeDay(models.Model):
    def __str__(self):
        return u"(%i) %s %s %s" % (self.id, self.event_attendee.attendee.FirstName,self.event_attendee.attendee.MiddleName,self.event_attendee.attendee.LastName)
    event_attendee = models.ForeignKey(EventAttendee, on_delete=models.CASCADE)
    day = models.IntegerField(default=0)
    datestamp = models.DateTimeField(null = True)