from django.db import models

class TimeSeriesData(models.Model):
 class Meta:
 app_label = 'foundation'
 db_table = 'BTC'
 verbose_name = _('BTC')
 verbose_name_plural = _('BTC')
 default_permissions = ()
 permissions = ()

 datetime = models.DateField()
 low = models.FloatField()
 high = models.FloatField()
 open = models.FloatField()
 close = models.FloatField()
 volume_from = models.FloatField()
 volume_to = models.FloatField()
 def __str__(self):
 return str(self.datetime) + " " + str(self.low) + " " + str(self.high) + " " + str(self.open) + " " +
str(self.close) + " " + str(self.volume_from) + " " + str(self.volume_to)
