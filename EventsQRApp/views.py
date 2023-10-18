from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Event, Attendee, EventAttendee
from openpyxl import Workbook, load_workbook
import pandas as pd
import random, string
from django.http import JsonResponse

# Create your views here.
def ImportExcelAttendees(request):
    if request.method == "POST":
        eventObj = Event.objects.get(pk = request.POST["events"])
        df = pd.read_excel(request.FILES["file"])
        idsArr = []
        for val in df.values.tolist():
            attendee = Attendee(FirstName=val[0],MiddleName=val[1],LastName=val[2])
            attendee.save()
            idsArr.append(attendee)
       
        for val in idsArr:
             qr = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
             event_attendee = EventAttendee(event=eventObj, attendee=val,qrcode=qr)
             event_attendee.save()

    
    events = Event.objects.all()
    data = {
        "events":events,
    }
    template = loader.get_template("EventsQRApp/import-attendees.html")
    return HttpResponse(template.render(data, request))

    # wb = Workbook()
    # ws = wb.active
    # ws['A1'] = 42
    # ws.append([1, 2, 3])
    # import datetime
    # ws['A2'] = datetime.datetime.now()
    # wb.save("sample.xlsx")
    # events = Event.objects.all()
    # data = {
    #     "events":events,
    # }
    # template = loader.get_template("EventsQRApp/import-attendees.html")
    # return HttpResponse(template.render(data, request))
def EventAttendeeQRCode(request,event_id):
    template = loader.get_template("EventsQRApp/event-attendee-qr.html")
    event = Event.objects.get(pk=event_id)
    event_attendees = EventAttendee.objects.filter(event=event)    
    data = {
        "event_attendees": event_attendees
    }
    return HttpResponse(template.render(data, request))

def ScanAttendeesQRCode(request,event_id):
    if request.method == "POST":
        return JsonResponse({'foo':request.POST["qrcode"]})

    template = loader.get_template("EventsQRApp/scan-attendee-qr.html")
    event = Event.objects.get(pk=event_id)
    data = {
        "event": event
    }
    return HttpResponse(template.render(data, request))