from django.contrib import admin
from django.urls import path

from . import views

app_name='events'
urlpatterns = [
    path('event-list',views.all_events,name="all_events"),
    path('event-add<int:id>',views.events_add,name="edit_event"),
    path('<int:id>/delete/', views.delete_event, name='delete_event'),

    path('event-add',views.events_add,name="eventadd"),
    path('view-event/<int:id>',views.view_event,name='view_event'),

    #homepage view of event
    path('all-events-index',views.index_all_events,name='index_all_events'),
    path('homepage-view-event/<int:id>',views.homepage_view_event,name='homepage_view_event'),
    #for participation
    path('participate/<int:event_id>/', views.participate, name='participate'),
    # path('participation/', views.regunauth, name="participation"),
    #payment for events
    path('event/payment/process/<int:event_id>/', views.auth_payment_process, name='auth_payment_process'),
    path('event/payment/process/<int:event_id>/<str:name>/<str:email>/<int:phone>', views.unauth_payment_process, name='unauth_payment_process'),
    # path('event/payment/done/', views.payment_done, name='payment_done'),

    # path('participation-list/', views.participatorlist, name='participation_list'),

    path('participation_list/', views.participatorlist, name='participation_list'),
    # URL pattern for showing participation list for a specific event
    path('participation_list/<int:event_id>/', views.participatorlist, name='event_participation_list'),
    path('not_going_participants/<int:event_id>/', views.not_going_participants, name='not_going_participants'),
]