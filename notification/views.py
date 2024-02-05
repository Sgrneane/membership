from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from account.models import CustomUser
from .models import (Notifications,Groups)
from .forms import CreateGroupForm,NotificationForm
from management.models import Membership, GeneralMembership,StudentMembership,InstitutionalMembership
from django.contrib import messages

# Create your views here.

def create_initial_group(request):
    """ Only to create group here. First"""
    verified_users = Membership.objects.select_subclasses().filter(verification=True)
    gm_users = Membership.objects.select_subclasses().filter(verification=True,membership_type =1)
    life_users = Membership.objects.select_subclasses().filter(verification=True,membership_type =3)
    st_users = Membership.objects.select_subclasses().filter(verification=True,membership_type =4)
    ins_users = Membership.objects.filter(verification=True,membership_type =2)
    a=Groups.objects.create(name='All Members',description="This group contains all registered members.")
    b=Groups.objects.create(name='General Members',description="This group contains all the members with general membership.")
    c=Groups.objects.create(name='Lifetime Members',description="This group contains all the members with lifetime membership.")
    d=Groups.objects.create(name='Student Members',description="This group contains all the members with student membership.")
    e=Groups.objects.create(name='Institutional Members',description="This group contains all the members with institutional membership.")
    a.users.set(verified_users.values_list('associated_user', flat=True))
    b.users.set(gm_users.values_list('associated_user', flat=True))
    c.users.set(life_users.values_list('associated_user', flat=True))
    d.users.set(st_users.values_list('associated_user', flat=True))
    e.users.set(ins_users.values_list('associated_user', flat=True))
    return HttpResponse("Seed Groups Created")

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

def create_notification(request):
    groups=Groups.objects.all()
    form = NotificationForm(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notification:all_notifications')
        else:
            print(form.errors)
    context={
        'groups':groups,
        'form':form
    }
    return render(request,'notification/create_notification.html',context)

def all_notifications(request):
    notifications= Notifications.objects.all()
    return render(request,'notification/all_notifications.html')


