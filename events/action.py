from django.db.models.signals import pre_save,post_save,m2m_changed
from django.dispatch import receiver
from .models import Event
from notification.notify import ThreadedNotification

# @receiver(m2m_changed, sender=Event.groups.through)
# def event_group_changed(sender, instance, action, model, **kwargs):
#     if action == "post_add" and instance.status == 1:# or action == "post_remove" or action == "post_clear":    
#         print("email  using m2m")
#         ThreadedNotification(instance,'Event')

# @receiver(pre_save,sender=Event)
# def event_post_save(sender,instance,**kwargs):
#     #to notify false,true,true,false
#     created = False
#     if not instance.pk:
#         created  = True
#     # print(created,Event.objects.get(id=instance.id).status != instance.status,instance.status,instance._is_m2m_changed)
#     if not created and Event.objects.get(id=instance.id).status != instance.status and instance.status == True and instance._is_m2m_changed == False:
#         print("email using post save ")
#         ThreadedNotification(instance,'Event')


@receiver(pre_save, sender=Event)
def event_pre_save(sender, instance, **kwargs):
    if instance.pk:  # Check if the instance already exists (i.e., it's an update)
        old_instance = Event.objects.get(pk=instance.pk)
        if old_instance.status != instance.status and instance.status:  # Compare statuses
            print("Sending notification for status change")
            ThreadedNotification(instance, 'Event')

@receiver(post_save, sender=Event)
def event_post_save(sender, instance, created, **kwargs):
    if created:  # Only notify on creation if needed
        print("Sending notification for new event creation")
        ThreadedNotification(instance, 'Event')



