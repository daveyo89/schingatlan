from django.contrib import admin
from House.models import Category, Property, PropertyImage, Data, City, Types, CityPart


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]


admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)
admin.site.register(Types)
admin.site.register(Data)
admin.site.register(City)
admin.site.register(CityPart)
