from django.urls import path

from . import views

urlpatterns = [
    path("import-attendees/", views.ImportExcelAttendees, name="ImportExcelAttendees"),
    path("event/<int:event_id>/attendees/", views.EventAttendeeQRCode, name="EventAttendeeQRCode"),
    path("event/<int:event_id>/scan-attendees/", views.ScanAttendeesQRCode, name="ScanAttendeesQRCode"),
]