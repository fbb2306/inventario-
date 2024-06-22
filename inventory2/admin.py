from django.contrib import admin

# Register your models here.
from inventory2.models import inventory

class inventoryadmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'brand', 'tool', 'specs',)
    search_fields = ('models',)
    
admin.site.register(inventory, inventoryadmin)











