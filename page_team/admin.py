from django.contrib import admin
from .models import TeamNews


class TeamNewsAdmin(admin.ModelAdmin):
    list_display = ('title' , 'datetime_created')


admin.site.register(TeamNews , TeamNewsAdmin)