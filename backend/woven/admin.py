from django.contrib import admin
from .models import CreateVirtualNuban, GetVirtualNuban, APIRequest
# Register your models here.


admin.site.register(CreateVirtualNuban)
admin.site.register(GetVirtualNuban)
admin.site.register(APIRequest)
