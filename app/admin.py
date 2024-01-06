from django.contrib import admin

from .models import *

# Register your models here.


class ForwardPhysicalValuesAdmin(admin.ModelAdmin):
    list_display = ("prod", "mar", "apr", "may", "q3")


class SeaborneLastTradedLevelsAdmin(admin.ModelAdmin):
    list_display = ("product", "primary", "secondary")


admin.site.register(ForwardPhysicalValues, ForwardPhysicalValuesAdmin)
admin.site.register(SeaborneLastTradedLevels, SeaborneLastTradedLevelsAdmin)
