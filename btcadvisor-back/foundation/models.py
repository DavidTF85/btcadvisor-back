from django.db import models
import uuid
from django.db import migrations, models
from django.contrib.auth.models import User
# Create your models here.
#1. create a model tname time seriesdata
#2. make sure it have the fields  (datetime,low,high,open,close,volumefrom,volumeto)
#3.make sure run python manage make migration
#4. pyhon manage.py migrate

#thats all


class TimeSeriesDatum(models.Model):

        date = models.DateTimeField()
        low =  models.FloatField()
        high =  models.FloatField()
        open =  models.FloatField()
        close =  models.FloatField()
        volume_from = models.FloatField()
        volume_to = models.FloatField()

        def __int__(self):
            return  int(self.datetime) + int(self.low) + int(self.high) + int(self.open) + int(self.close) + int(self.volume_from) + int(self.volume_to)
