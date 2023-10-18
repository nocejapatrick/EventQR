from django.urls import path

from . import views

urlpatterns = [
    path("import-attendees/", views.ImportExcelAttendees, name="ImportExcelAttendees"),
    path("event/<int:event_id>/generate-attendee-qrcode/", views.GenerateQRCodeAttendee, name="GenerateQRCodeAttendee"),
    path("event/<int:event_id>/attendees/", views.EventAttendeeQRCode, name="EventAttendeeQRCode"),
    path("event/<int:event_id>/<int:day_id>/scan-attendees/", views.ScanAttendeesQRCode, name="ScanAttendeesQRCode"),
    path("event/<int:event_id>/<int:attendee_id>/display-qrcode/", views.DisplayGeneratedQRCode, name="DisplayGeneratedQRCode"),
]