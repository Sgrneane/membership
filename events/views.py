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
        g=request.POST['groups']
        print(g)
        if form.is_valid():
            event = form.save()
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