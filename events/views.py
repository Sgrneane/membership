from django.shortcuts import render,get_object_or_404,redirect
from .models import Event, Participation, TicketType
from notification.models import Groups
from .form import EventForm, TicketTypeFormSet, TicketTypeForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse
from account.models import CustomUser
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
import json




# Create your views here.

def all_events(request):
    data = {
        'events':Event.objects.all()
    }
    print(data)
    return render(request,'event/all_events.html',data)


# def events_add(request, id=None):
#     if id:
#         event = get_object_or_404(Event, id=id)
#         form = EventForm(request.POST or None, request.FILES or None, instance=event)
#     else:
#         event = None
#         form = EventForm(request.POST or None, request.FILES or None)

#     if request.method == 'POST':
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.veneu = request.POST.get('veneu', None)
#             event.url_location = request.POST.get('url_location', None)
#             event.description = request.POST.get('description', None)
#             event.guest_description = request.POST.get('guest_description', None)
#             event.ticket_pricing_description = request.POST.get('ticket_pricing_description', None)
#             event.pricing_type = request.POST.get('pricing_type', None)
            
#             # Check if the event is free
#             if event.pricing_type == 'free':
#                 # If it's free, set pricing fields to None
#                 event.pricing_normal = None
#                 event.pricing_vip = None
#                 event.pricing_vvip = None
#             else:
#                 # If it's paid, set pricing fields from form data
#                 event.pricing_normal = request.POST.get('pricing_normal', None)
#                 event.pricing_vip = request.POST.get('pricing_vip', None)
#                 event.pricing_vvip = request.POST.get('pricing_vvip', None)
            
#             event.save()
#             return redirect('events:all_events')
#         else:
#             print(form.errors)

#     data = {
#         'form': form,
#         'groups': Groups.objects.all(),
#         'event': event
#     }
#     return render(request, 'event/event-create.html', data)

def events_add(request, id=None):
    event = get_object_or_404(Event, id=id) if id else None
    
    if request.method == 'POST':
        event_form = EventForm(request.POST, request.FILES, instance=event)
      
        ticket_type_names = request.POST.getlist('ticket_type_name[]')
        ticket_type_descriptions = request.POST.getlist('ticket_type_description[]')
        ticket_type_limits = request.POST.getlist('ticket_type_limit[]')
        ticket_type_prices = request.POST.getlist('ticket_type_price[]')
        
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.save()
            
            for ticket_type_name, ticket_type_description, ticket_type_price, ticket_type_limit in zip(
                ticket_type_names,ticket_type_descriptions,ticket_type_prices,ticket_type_limits):
                
                form_data={
                    'name': ticket_type_name,
                    'description': ticket_type_description,
                    'limit': ticket_type_limit,
                    'price': ticket_type_price,
                    'event': event.id,
                }
                
                ticket_type_form= TicketTypeForm(form_data)
                
                if ticket_type_form.is_valid():
                    ticket_type_form.save()
                else:
                    print("Ticket Type Form Errors:", ticket_type_form.errors)
                    return redirect('events:all_events')  # Redirect outside the loop
        
            return redirect('events:all_events')
        else:
            print("Event Form Errors:", event_form.errors)
            print("Event Form Non-Field Errors:", event_form.non_field_errors())
    else:
        event_form = EventForm(instance=event)
    
    return render(request, 'event/event-create.html', {'event_form': event_form, 'groups': Groups.objects.all(), 'event': event})

def view_event(request,id):
    event= get_object_or_404(Event, id=id)
    remaining_groups = Groups.objects.exclude(events=event)

    if request.method == 'POST':
        opt = request.POST.get('hello')
        print(opt)
        if opt == '2':  # Comparing strings instead of integers
            user = request.user
            try:
                # Check if a Participation object already exists for the user and event
                existing_participation = Participation.objects.get(event=event, user=user)
                print("Participation already exists")
            except Participation.DoesNotExist:
                # Create a new Participation object only if it doesn't already exist
                party = Participation.objects.create(event=event, user=user, not_interested=True)
                print(party)
                print(user)
                party.save()
                print("done")
        return redirect('events:all_events')
    context={
        'event': event,
        'groups':remaining_groups,
    }
    return render(request,'event/view_event.html',context)

def homepage_view_event(request,id):
    event= get_object_or_404(Event, id=id)
    if Participation.objects.filter(event=event, email=request.POST.get('email')).exists():
        return HttpResponse("You have already participated in this event")
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        if event.is_paid_event():
            return redirect(reverse('events:unauth_payment_process', kwargs={'event_id': id, 'name': name,'email':email, 'phone': phone}))
        else:

            party = Participation.objects.create(event=event, name=name, email=email, phone_number=phone)
            print(party)
            party.save()
            return redirect('events:all_events')
    context={
        'event': event,
    }
    return render(request,'event/homepage/view_event.html',context)

def index_all_events(request):
    data = {
        'events':Event.objects.all()
    }
    return render(request,'event/index_events.html',data)

def participate(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if request.user.is_authenticated:
        # User is authenticated, check if the user has already participated
        if Participation.objects.filter(event=event, user=request.user).exists():
            return HttpResponse("You have already participated in this event")
        
        if event.is_paid_event():
            return redirect('events:auth_payment_process', event_id=event_id)
        else: 
            Participation.objects.create(event=event, user=request.user)
            return redirect('events:all_events')
    else:
        # Redirect to registration page with event_id as a query parameter
        return redirect(reverse('events:participation') + f'?event_id={event_id}')


# def unauth_payment_process(request, event_id, name, email, phone):
#     event = get_object_or_404(Event, id=event_id)
    
#     if Participation.objects.filter(event=event, email=email).exists():
#         return HttpResponse("You have already participated in this event")

#     if request.method == 'POST':
#         ticket_type = request.POST.get('ticket_type')  # Get selected ticket type
#         amount_paid = event.get_ticket_prices().get(ticket_type, 0)  # Get the price for the selected ticket type
        
#         # Handle file upload
#         payment_screenshot = request.FILES.get('payment_ss')

#         # Create Participation object
#         Participation.objects.create(event=event, name=name, email=email, phone_number=phone, ticket_type=ticket_type, amount_paid=amount_paid,payment_screenshot=payment_screenshot)
        
#         # Redirect to the all events page
#         return render(request, 'event/payment_process.html', {'amount_paid': amount_paid,'event':event,'name': name})
#     else:
#         return render(request, 'event/payment_process.html', {'event': event,'name': name})




# def auth_payment_process(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
    
#     if Participation.objects.filter(event=event, user=request.user).exists():
#         return HttpResponse("You have already participated in this event")
    
#     if request.method == 'POST':
#         ticket_type = request.POST.get('ticket_type')  # Get selected ticket type
#         amount_paid = event.get_ticket_prices().get(ticket_type, 0)  # Get the price for the selected ticket type
#         payment_screenshot = request.FILES.get('payment_ss')

        
        
#         # Create Participation object
#         Participation.objects.create(event=event, user=request.user, ticket_type=ticket_type, amount_paid=amount_paid,payment_screenshot=payment_screenshot)
        
#         # Redirect to the all events page
#         return render(request, 'event/payment_process.html', {'amount_paid': amount_paid,'event':event,'name': request.user.full_name})
#     else:
#         return render(request, 'event/payment_process.html', {'event': event,'name': request.user.full_name})


def unauth_payment_process(request, event_id, name, email, phone):
    event = get_object_or_404(Event, id=event_id)
    ticket_types = TicketType.objects.filter(event=event)

    if request.method == 'POST':
        name = name
        email = email
        phone = phone
        ticket_type_id = request.POST.get('ticket_type')
        ticket_type = get_object_or_404(TicketType, pk=ticket_type_id)
        amount_paid = ticket_type.price
        payment_screenshot = request.FILES.get('payment_ss')

        if Participation.objects.filter(event=event, email=email).exists():
            return HttpResponse("You have already participated in this event")

        Participation.objects.create(event=event, name=name, email=email, phone_number=phone, ticket_type=ticket_type, amount_paid=amount_paid, payment_screenshot=payment_screenshot)
        
        # Redirect to the payment process confirmation page
        return render(request, 'event/payment_process.html', {'amount_paid': amount_paid, 'event': event, 'name': name})
    else:
        return render(request, 'event/payment_process.html', {'event': event, 'ticket_types': ticket_types ,'name':name})


def auth_payment_process(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    ticket_types = TicketType.objects.filter(event=event)

    if request.method == 'POST':
        ticket_type_id = request.POST.get('ticket_type')  # Get selected ticket type id
        ticket_type = get_object_or_404(TicketType, pk=ticket_type_id)
        amount_paid = ticket_type.price
        payment_screenshot = request.FILES.get('payment_ss')

        if Participation.objects.filter(event=event, user=request.user).exists():
            return HttpResponse("You have already participated in this event")
        
        # Create Participation object
        Participation.objects.create(event=event, user=request.user, ticket_type=ticket_type, amount_paid=amount_paid, payment_screenshot=payment_screenshot)
        
        # Redirect to the payment process confirmation page
        return render(request, 'event/payment_process.html', {'amount_paid': amount_paid, 'event': event, 'name': request.user.full_name})
    else:
        return render(request, 'event/payment_process.html', {'event': event, 'ticket_types': ticket_types, 'name': request.user.full_name})



def participatorlist(request, event_id=None):
    if request.user.role == CustomUser.ADMIN:
        if event_id:
            event = Event.objects.get(id=event_id)
            participator_auth_going = Participation.objects.filter(event=event, user__isnull=False, not_interested=False)
            # participator_auth_not_interested = Participation.objects.filter(event=event, user__isnull=False, not_interested=True)
            participator_non_auth = Participation.objects.filter(event=event, user__isnull=True)
            return render(request, 'event/list.html', {
                'participator_auth_going': participator_auth_going,
                # 'participator_auth_not_interested': participator_auth_not_interested,
                'participator_non_auth': participator_non_auth,
                'event': event
            })
        else:
            events = Event.objects.all()
            return render(request, 'event/event_list.html', {'events': events})
    else:
        return HttpResponse("You are not authorized to view this page")
    

def not_going_participants(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # Check if the user has permission to view the page
    if request.user.is_authenticated and request.user.role == 1:
        # Filter participants who are not interested in the event
        not_going_participants = Participation.objects.filter(event=event, not_interested=True)
                
        return render(request, 'event/not_going_participants.html', {
            'not_going_participants': not_going_participants,
            'event': event
        })
    else:
        return HttpResponse("You are not authorized to view this page")

