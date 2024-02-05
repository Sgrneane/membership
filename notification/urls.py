from django.contrib import admin
from django.urls import path

from . import views

app_name='notification'
urlpatterns = [
    path('create-group',views.create_group,name='create_group'),
    path('all-groups',views.all_groups,name='all_groups'),
    path('view-group/<int:id>',views.view_group,name='view_group'),
    path('create-notification',views.create_notification,name='create_notification'),
    path('all-notifications',views.all_notifications,name='all_notifications'),
]
