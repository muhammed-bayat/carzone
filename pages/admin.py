from django.contrib import admin

# Register your models here.
from pages.models import Team
from django.utils.html import format_html







class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{url}" width="50" height="50" />'.format(url=obj.photo.url))
        else:
            return "-"


    list_display = ('id','thumbnail', 'first_name', 'designation',"created_date")
    list_display_links = ('id', 'first_name', 'designation')
    list_filter = ('designation',)
    search_fields = ('first_name', 'designation')
    list_per_page = 25




admin.site.register(Team,TeamAdmin)
