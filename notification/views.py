from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from account.models import CustomUser
from .models import (Notifications,Groups)
from .forms import CreateGroupForm,NotificationForm
from management.models import Membership, GeneralMembership,InstitutionalMembership
from django.contrib import messages

# Create your views here.

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Groups

def create_or_update_groups(request):
    group_names = [
        ('All Members', "This group contains all registered members."),
        ('General Members', "This group contains all the members with general membership."),
        ('Lifetime Members', "This group contains all the members with lifetime membership."),
        ('Student Members', "This group contains all the members with student membership."),
        ('Institutional Members', "This group contains all the members with institutional membership."),
    ]

    groups = {}
    for name, description in group_names:
        group, created = Groups.objects.get_or_create(name=name, defaults={'description': description})
        groups[name] = group

    verified_users = Membership.objects.select_subclasses().filter(verification=True)
    gm_users = verified_users.filter(membership_type=1)
    life_users = verified_users.filter(membership_type=3)
    st_users = verified_users.filter(membership_type=4)
    ins_users = Membership.objects.filter(verification=True, membership_type=2)

    groups['All Members'].users.set(verified_users.values_list('associated_user', flat=True))
    groups['General Members'].users.set(gm_users.values_list('associated_user', flat=True))
    groups['Lifetime Members'].users.set(life_users.values_list('associated_user', flat=True))
    groups['Student Members'].users.set(st_users.values_list('associated_user', flat=True))
    groups['Institutional Members'].users.set(ins_users.values_list('associated_user', flat=True))

    return HttpResponse("Groups Created or Updated")

def update_missing_members():
    verified_users = Membership.objects.select_subclasses().filter(verification=True)
    
    for user in verified_users:
        group_name = 'All Members'
        if user.membership_type == 1:
            group_name = 'General Members'
        elif user.membership_type == 2:
            group_name = 'Institutional Members'
        elif user.membership_type == 3:
            group_name = 'Lifetime Members'
        elif user.membership_type == 4:
            group_name = 'Student Members'

        group = Groups.objects.get(name=group_name)
        if not group.users.filter(id=user.associated_user.id).exists():
            group.users.add(user.associated_user.id)

    return HttpResponse("Missing Members Updated")

def create_or_update_groups_and_missing_members(request):
    create_or_update_groups(request)
    update_missing_members()
    return HttpResponse("Groups Created/Updated and Missing Members Updated")


# def create_initial_group(request):
#     """ Only to create group here. First"""
#     verified_users = Membership.objects.select_subclasses().filter(verification=True)
#     gm_users = Membership.objects.select_subclasses().filter(verification=True,membership_type =1)
#     life_users = Membership.objects.select_subclasses().filter(verification=True,membership_type =3)
#     st_users = Membership.objects.select_subclasses().filter(verification=True,membership_type =4)
#     ins_users = Membership.objects.filter(verification=True,membership_type =2)
#     a=Groups.objects.create(name='All Members',description="This group contains all registered members.")
#     b=Groups.objects.create(name='General Members',description="This group contains all the members with general membership.")
#     c=Groups.objects.create(name='Lifetime Members',description="This group contains all the members with lifetime membership.")
#     d=Groups.objects.create(name='Student Members',description="This group contains all the members with student membership.")
#     e=Groups.objects.create(name='Institutional Members',description="This group contains all the members with institutional membership.")
#     a.users.set(verified_users.values_list('associated_user', flat=True))
#     b.users.set(gm_users.values_list('associated_user', flat=True))
#     c.users.set(life_users.values_list('associated_user', flat=True))
#     d.users.set(st_users.values_list('associated_user', flat=True))
#     e.users.set(ins_users.values_list('associated_user', flat=True))
#     return HttpResponse("Seed Groups Created")

def create_group(request,id=None):
    all_users = CustomUser.objects.all()
    if id:
        group = get_object_or_404(Groups, id=id)
        form = CreateGroupForm(request.POST or None, instance=group)
    else:
        group=None
        form = CreateGroupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            group= form.save()
            if id:
                messages.success(request, 'Notification mailing group updated successfully.')
            else:
                messages.success(request, 'Notification mailing group created successfully.')
            return redirect('notification:all_groups')
        else:
            print(form.errors)
    else:
        pass
    context={
        'all_users':all_users,
        'form':form,
        'group':group
    }
    return render(request,'notification/create_group.html',context)

def all_groups(request):
    groups= Groups.objects.all()
    context={
        'groups':groups,
    }
    return render(request,'notification/all_groups.html',context)

def view_group(request,id):
    group=get_object_or_404(Groups,id=id)
    context={
        'group': group,
    }
    return render(request,'notification/view_group.html',context)

def delete_group(request, id):
    group = get_object_or_404(Groups, id=id)
    if request.method == "POST":
        group.delete()
        messages.success(request, "Notification mailing group deleted successfully.")
    return redirect('notification:all_groups')

# def create_notification(request,id=None):
#     groups = Groups.objects.all()
    
#     # If id is provided, retrieve the notification instance
#     notification_instance = None
#     if id:
#         notification_instance = get_object_or_404(Notifications, id=id)
#     form = NotificationForm(request.POST or None,request.FILES or None,instance=notification_instance)
#     if request.method == 'POST':
#         print(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('notification:all_notifications')
#         else:
#             print(form.errors)
#     context={
#         'groups':groups,
#         'form':form
#     }
#     return render(request,'notification/create_notification.html',context)

def create_notification(request, id=None):
    groups = Groups.objects.all()

    # If id is provided, retrieve the notification instance
    notification_instance = None
    if id:
        notification_instance = get_object_or_404(Notifications, id=id)
    form = NotificationForm(request.POST or None, request.FILES or None, instance=notification_instance)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.status = request.POST.get('status') == '1'
            notification.save()
            form.save_m2m()
            return redirect('notification:all_notifications')
        else:
            print(form.errors)
    context = {
        'groups': groups,
        'form': form
    }
    return render(request, 'notification/create_notification.html', context)


def all_notifications(request):
    notifications= Notifications.objects.all()
    context={
        'notifications':notifications,
    }
    return render(request,'notification/all_notifications.html',context)


def view_notification(request,id):
    notification_instance = get_object_or_404(Notifications, id=id)
    context={
        'notification':notification_instance
    }
    return render(request,'notification/view_notification.html',context)




