from django.contrib import admin
from cms.models import Domain,ConvertParam

# Register your models here.

class DomainAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'ip',)
	list_display_links = ('id', 'name', 'ip',)
admin.site.register(Domain, DomainAdmin)


class ConvertParamAdmin(admin.ModelAdmin):
	list_display = ('id', 'key', 'value',)
	list_display_links = ('id', 'key', 'value',)
admin.site.register(ConvertParam, ConvertParamAdmin)
