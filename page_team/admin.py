from django.contrib import admin
from .models import TeamNews , TeamShop , TeamGallery , TeamPlayer


class TeamNewsAdmin(admin.ModelAdmin):
    list_display = ('title' , 'datetime_created')

class TeamShopAdmin(admin.ModelAdmin):
    list_display = ('title' , 'datetime_created' , 'price')


admin.site.register(TeamNews , TeamNewsAdmin)
admin.site.register(TeamShop , TeamShopAdmin)
admin.site.register(TeamGallery , TeamNewsAdmin)
admin.site.register(TeamPlayer )

