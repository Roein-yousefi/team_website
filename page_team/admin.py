from django.contrib import admin
from .models import TeamNews


class TeamNewsAdmin(admin.ModelAdmin):
    list_display = ('title')


admin.site.register(TeamNews)