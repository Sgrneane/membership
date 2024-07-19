from django.contrib import admin
from .models import Notifications,Groups

class NotificationsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'id')

    def save_model(self, request, obj, form, change):
        kwargs = {'extra_data': 'extra'}
        if not change:
            # This means the object is being created
            print(f'Notifications instance "{obj.subject}" is being created.')
        else:
            form_groups = [int(group) for group in request.POST.getlist('groups')]
            instance_groups = list(obj.groups.all().values_list('id',flat = True))
            if form_groups == instance_groups:
                obj._is_m2m_changed = False #if changed and draft to sent then notify
                # print("false , it is not changed")
            else:
                obj._is_m2m_changed = True #if changed then not notify
                # print("false , it is changed")

        super().save_model(request, obj, form, change)

admin.site.register(Notifications, NotificationsAdmin)

# admin.site.register(Notifications)
admin.site.register(Groups)