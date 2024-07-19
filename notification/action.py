from django.db.models.signals import pre_save,post_save,m2m_changed
from django.dispatch import receiver
from .models import Notifications
from .notify import ThreadedNotification

# @receiver(m2m_changed, sender=Notifications.groups.through)
# def notification_group_changed(sender, instance, action, model, **kwargs):
#     if action == "post_add" and instance.status == 1:# or action == "post_remove" or action == "post_clear":    
#         print("email  using m2m")
#         ThreadedNotification(instance,'Notifications')

# @receiver(pre_save,sender=Notifications)
# def notification_post_save(sender,instance,**kwargs):
#     #to notify false,true,true,false
#     created = False
#     if not instance.pk:
#         created  = True
#     # print(created,Notifications.objects.get(id=instance.id).status != instance.status,instance.status,instance._is_m2m_changed)
#     if not created and Notifications.objects.get(id=instance.id).status != instance.status and instance.status == True and instance._is_m2m_changed == False:
#         print(" email using post save ")
#         ThreadedNotification(instance,'Notifications')

@receiver(m2m_changed, sender=Notifications.groups.through)
def notification_group_changed(sender, instance, action, model, **kwargs):
    if action == "post_add" and instance.status:
        print("email using m2m")
        ThreadedNotification(instance, 'Notifications')

@receiver(pre_save, sender=Notifications)
def notification_pre_save(sender, instance, **kwargs):
    created = not instance.pk
    if not created and Notifications.objects.get(id=instance.id).status != instance.status and instance.status:
        print("email using pre save")
        ThreadedNotification(instance, 'Notifications')




