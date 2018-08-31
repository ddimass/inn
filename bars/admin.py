from django.contrib import admin

from .models import Bars

@admin.register(Bars)
class BarsAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'timeframe', 'timestamp', 'open', 'close', 'high', 'low', 'tick_volume')
    list_filter = ('symbol', 'timeframe', 'timestamp')
# Register your models here.
