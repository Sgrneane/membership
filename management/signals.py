# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ActionLog, CustomUser, NationalDocumment, EducationalDocuments, Membership, Payment
from .models import NationalDocumment, EducationalDocuments, ActionLog, GeneralMembership


def log_action(user, action):
    ActionLog.objects.create(user=user, action=action)

@receiver(post_save, sender=CustomUser)
def log_user_registration(sender, instance, created, **kwargs):
    if created:
        log_action(instance, "User registered")

@receiver(post_save, sender=NationalDocumment)
def log_national_document(sender, instance, created, **kwargs):
    if not created:
        return

    action = "Created national document"
    
    try:
        membership = GeneralMembership.objects.get(nationaldocument=instance)
        log_action(membership.associated_user, action)
    except GeneralMembership.DoesNotExist:
        print(f"No associated_membership found for NationalDocumment instance {instance.id}")
        # Add debugging
        print(f"NationalDocumment instance: {instance}")

@receiver(post_save, sender=EducationalDocuments)
def log_educational_document(sender, instance, created, **kwargs):
    if not created:
        return

    action = "Created educational document"
    
    try:
        membership = GeneralMembership.objects.get(educational_information=instance)
        log_action(membership.associated_user, action)
    except GeneralMembership.DoesNotExist:
        print(f"No associated_membership found for EducationalDocuments instance {instance.id}")
        # Add debugging
        print(f"EducationalDocuments instance: {instance}")

# @receiver(post_save, sender=GeneralMembership)
# def log_general_membership_update(sender, instance, created, **kwargs):
#     if created:
#         return

#     if hasattr(instance, 'nationaldocument'):
#         national_document = instance.nationaldocument
#         if national_document:
#             log_action(instance.associated_user, "Created national document")

#     if hasattr(instance, 'educational_information'):
#         educational_document = instance.educational_information
#         if educational_document:
#             log_action(instance.associated_user, "Created educational document") 

 
@receiver(post_save, sender=Membership)
def log_membership(sender, instance, created, **kwargs):
    action = "Applied for membership" if created else "Updated membership"
    log_action(instance.associated_user, action)

@receiver(post_save, sender=Payment)
def log_payment(sender, instance, created, **kwargs):
    action = "Made payment" if created else "Updated payment"
    log_action(instance.created_by, action)
