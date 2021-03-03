from django.db import models

# Create your models here.


class CreateVirtualNuban(models.Model):
    body = models.JSONField()
    bank_name = models.CharField(max_length=400)
    vnuban = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.vnuban


class GetVirtualNuban(models.Model):
    body = models.JSONField()

    def __str__(self) -> str:
        return str(self.id)


class APIRequest(models.Model):

    call_type = models.CharField(max_length=100)
    start_time = models.CharField(max_length=400)
    end_time = models.CharField(max_length=400)
    status = models.CharField(max_length=100, choices=(('successful', 'successful'), ('failed', 'failed')))
    status_message = models.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.call_type + ' ' + str(self.created_on)
