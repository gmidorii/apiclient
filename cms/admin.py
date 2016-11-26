from django.contrib import admin
from cms.models import Domain

# Register your models here.

class DomainAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'ip',)
	list_display_links = ('id', 'name', 'ip',)
admin.site.register(Domain, DomainAdmin)
