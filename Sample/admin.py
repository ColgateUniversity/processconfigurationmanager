from django.contrib import admin

from .models import processInfo
from .models import processElements
from .models import groupInfo
from .models import processAccessInfo
from .models import processUpdateLog
from .models import scheduledUpdatesInfo

admin.site.site_header = "Process Configuration Manager - Admin"
admin.site.site_title = "Process Configuration Manager - Admin"
admin.site.index_title = ""

class Process_Admin_Model(admin.ModelAdmin):
    fields_to_display = ("Process ID", "Process Name", "Process Description", "")

admin.site.register(processInfo, Process_Admin_Model)
admin.site.register(processElements)
admin.site.register(groupInfo)
admin.site.register(processAccessInfo)
admin.site.register(processUpdateLog)
admin.site.register(scheduledUpdatesInfo)


