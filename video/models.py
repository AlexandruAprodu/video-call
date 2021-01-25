from django.db import models

# Create your models here.


class Keys(models.Model):
    AppId = models.CharField(max_length=300)
    Channel = models.CharField(max_length=300)
    appCertificate = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Keys"

