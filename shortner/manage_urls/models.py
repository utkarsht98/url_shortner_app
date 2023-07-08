from django.db import models


# Create your models here.
class Urlinfo(models.Model):
    uuid = models.BigIntegerField(unique=True, primary_key=True)
    longUrl = models.CharField(max_length=300, null=False)
    shortUrl = models.CharField(max_length=100, null=False)
