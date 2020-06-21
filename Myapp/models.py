from django.db import models
import pytz
from timezone_field import TimeZoneField

class User(models.Model):
    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)