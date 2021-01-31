from django.contrib import admin
from House.models import Category, Property, PropertyImage, Data, City


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Data)
admin.site.register(City)
