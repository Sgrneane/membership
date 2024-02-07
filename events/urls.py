from django.contrib import admin
from django.urls import path

from . import views

app_name='events'
urlpatterns = [
    path('event-list',views.all_events , name="all_events"),
    path('event-add<int:id>',views.events_add , name="edit_event"),
    path('event-add',views.events_add , name="eventadd"),
    path('view-event/<int:id>',views.view_event,name='view_event')
]