from django.contrib import admin
from .models import VirtualNuban, GetVirtualNuban, APIRequest
# Register your models here.


admin.site.register(VirtualNuban)
admin.site.register(GetVirtualNuban)
admin.site.register(APIRequest)
