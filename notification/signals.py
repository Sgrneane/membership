from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import  Groups
from management.models import Membership

@receiver(post_save, sender=Membership)
def add_to_group(sender, instance, created, **kwargs):
    if instance.verification:  # Check if the membership is verified
        user_id = instance.associated_user.id
        all_members_group, _ = Groups.objects.get_or_create(name='All Members', defaults={'description': "This group contains all registered members."})
        all_members_group.users.add(user_id)

        if instance.membership_type == 1:
            group, _ = Groups.objects.get_or_create(name='General Members', defaults={'description': "This group contains all the members with general membership."})
        elif instance.membership_type == 2:
            group, _ = Groups.objects.get_or_create(name='Institutional Members', defaults={'description': "This group contains all the members with institutional membership."})
        elif instance.membership_type == 3:
            group, _ = Groups.objects.get_or_create(name='Lifetime Members', defaults={'description': "This group contains all the members with lifetime membership."})
        elif instance.membership_type == 4:
            group, _ = Groups.objects.get_or_create(name='Student Members', defaults={'description': "This group contains all the members with student membership."})
        else:
            group = None

        if group:
            group.users.add(user_id)
