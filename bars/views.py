from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bars.models import Bars
from bars.serializers import BarsSerializer
from rest_framework.parsers import JSONParser
from datetime import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def bars_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        bars = Bars.objects.all()
        serializer = BarsSerializer(bars, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BarsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# Create your views here.
def bars_set(request):
    if request.GET.keys() != {'symbol', 'timeframe', 'timestamp', 'open', 'close', 'high', 'low', 'tick_volume'}:
        return HttpResponse("You set not all fields:  symbol, timeframe, timestamp, open, close, high, low, tick_volume")
    else:
        ts = datetime.utcfromtimestamp(int(request.GET['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')
        bar = Bars(symbol = request.GET['symbol'],
                   timeframe = request.GET['timeframe'],
                   timestamp = ts,
                   open = request.GET['open'],
                   close = request.GET['close'],
                   high = request.GET['high'],
                   low = request.GET['low'],
                   tick_volume = request.GET['tick_volume'])
        bar.save()
        return HttpResponse(request.GET['symbol'] + ' saved')
