from django.contrib import admin
from .models import ItemModel

# Register your models here.
class menuItemAdmin(admin.ModelAdmin):
    list_display = ("meal","meal_type","status", )
    list_filter = ("status","meal_type")
    search_fields = ("meal","description","meal_type")

admin.site.register(ItemModel,menuItemAdmin)