from django.db import models
timeframes = (
    (1, 'M1'),
    (2, 'M5'),
    (3, 'M15'),
    (4, 'M30'),
    (5, 'H1'),
    (6, 'H4'),
    (7, 'D1'),
    (8, 'W1'),
    (9, 'MN'),
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
        return self.symbol
