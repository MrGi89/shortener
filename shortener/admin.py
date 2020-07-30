from django.contrib import admin

from shortener.models import UrlModel


class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('slug', 'url',)
    list_per_page = 50


admin.site.register(UrlModel, UrlModelAdmin)
