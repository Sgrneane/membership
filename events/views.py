from django.shortcuts import render,get_object_or_404,redirect
from .models import Event
from notification.models import Groups
from .form import EventForm
from django.contrib import messages


# Create your views here.

def all_events(request):
    data = {
        'events':Event.objects.all()
    }
    print(data)
    return render(request,'event/all_events.html',data)

def events_add(request,id=None):

    if id:
        event = get_object_or_404(Event, id=id)
        form = EventForm(request.POST or None, request.FILES or None, instance=event)
    else:
        event=None
        form = EventForm(request.POST or None,request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            veneu=request.POST.get('veneu',None)
            url_location=request.POST.get('url_location',None)
            description=request.POST.get('description',None)
            guest_description=request.POST.get('guest_description',None)
            ticket_pricing_description=request.POST.get('ticket_pricing_description',None)

            event = form.save()
            event.veneu=veneu
            event.url_location= url_location
            event.description = description
            event.guest_description = guest_description
            event.ticket_pricing_description=ticket_pricing_description
            event.save()
            return redirect('events:all_events')
        else:
            print(form.errors)
    else:
        pass
        
    data = {
        'form':form,
        'groups':Groups.objects.all(),
        'event':event
    }
    # print(data)
    return render(request,'event/event-create.html',data)


def view_event(request,id):
    event= get_object_or_404(Event, id=id)
    remaining_groups = Groups.objects.exclude(events=event)
    context={
        'event': event,
        'groups':remaining_groups,
    }
    return render(request,'event/view_event.html',context)

def homepage_view_event(request,id):
    event= get_object_or_404(Event, id=id)
    context={
        'event': event,
    }
    return render(request,'event/homepage/view_event.html',context)

def index_all_events(request):
    data = {
        'events':Event.objects.all()
    }
    return render(request,'event/index_events.html',data)
