from django.db import models
timeframes = (
    (0, 'M1'),
    (1, 'M5'),
    (2, 'M15'),
    (3, 'M30'),
    (4, 'H1'),
    (5, 'H4'),
    (6, 'D1'),
    (7, 'W1'),
    (8, 'MN'),
)
class Bars(models.Model):
    symbol = models.CharField(max_length=15)
    timeframe = models.IntegerField(choices=timeframes)
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    tick_volume = models.IntegerField()

    def __str__(self):
        return self.symbol + " - " + str(self.timeframe) + " - " + str(self.timestamp)

