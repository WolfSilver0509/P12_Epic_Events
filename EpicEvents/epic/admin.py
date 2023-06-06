
from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'company_name')
    list_filter = ('date_created', 'date_updated')
    search_fields = ('first_name', 'last_name', 'email', 'company_name')

admin.site.register(Client, ClientAdmin)
