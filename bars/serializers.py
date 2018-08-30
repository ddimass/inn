from bars.models import Bars, timeframes
from rest_framework import serializers


class BarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bars
        fields = ('symbol', 'timeframe', 'timestamp', 'open', 'high', 'low', 'close', 'tick_volume')
