from django.contrib import admin
from .models import CreateVirtualNuban, GetVirtualNuban
# Register your models here.


admin.site.register(CreateVirtualNuban)
admin.site.register(GetVirtualNuban)
