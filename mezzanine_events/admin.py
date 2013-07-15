from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Event, EventContainer
from copy import deepcopy
from django.utils.translation import ugettext_lazy as _
# event_admin_fieldsets = deepcopy(PageAdmin.fieldsets)
# event_admin_fieldsets[0][1]["fields"]

class EventAdmin (PageAdmin):
	fieldsets = (
		deepcopy(PageAdmin.fieldsets[0]),
		(_("Event details"),{
			'fields': ('content', 'date', ('start_time', 'end_time'), 'location', 'mappable_location', ('lat', 'lon'), 'speakers', 'rsvp')
		}),
		deepcopy(PageAdmin.fieldsets[1]),
	)

admin.site.register(Event, EventAdmin)

admin.site.register(EventContainer, PageAdmin)
