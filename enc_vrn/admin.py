from django.contrib import admin
from .models import Architect,Address,Excursion, Sight

@admin.register(Architect)
class ArchitectAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAddress(admin.ModelAdmin):
    pass

@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    pass

@admin.register(Excursion)
class ExcursionAdmin(admin.ModelAdmin):
    pass