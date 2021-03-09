from django.contrib import admin
from .models import CreateVirtualNuban, GetVirtualNuban, APIRequest, MandateId
# Register your models here.


admin.site.register(CreateVirtualNuban)
admin.site.register(GetVirtualNuban)
admin.site.register(APIRequest)
admin.site.register(MandateId)
