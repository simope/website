from django.db import models

# Create your models here.
class rps_match(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=10)

class user(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=100)
    name = models.CharField(max_length=255, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    points = models.BigIntegerField(null=True)