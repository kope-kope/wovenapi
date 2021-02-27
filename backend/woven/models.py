from django.db import models

# Create your models here.


class VirtualNuban(models.Model):
    body = models.JSONField()
    bank_name = models.CharField(max_length=400)
    vnuban = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.vnuban


class GetVirtualNuban(models.Model):
    body = models.JSONField()

    def __str__(self) -> str:
        return str(self.id)