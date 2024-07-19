from django.contrib import admin
from .models import Event, Participation, TicketType
from .form import EventForm

class TicketTypeInline(admin.TabularInline):
    model = TicketType
    extra = 1

class EventAdmin(admin.ModelAdmin):
    form = EventForm 
    inlines = [TicketTypeInline] # Use custom form

    list_display = ('name', 'id')

    def save_model(self, request, obj, form, change):
        if not change:
            # This means the object is being created
            print(f'Event instance "{obj.name}" is being created.')
        else:
            form_groups = [int(group) for group in request.POST.getlist('groups')]
            instance_groups = list(obj.groups.all().values_list('id', flat=True))
            if form_groups == instance_groups:
                obj._is_m2m_changed = False #if changed and draft to sent then notify
            else:
                obj._is_m2m_changed = True #if changed then not notify

        super().save_model(request, obj, form, change)

admin.site.register(Event, EventAdmin)
admin.site.register(TicketType)
admin.site.register(Participation)
