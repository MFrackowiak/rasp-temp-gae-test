# Create your views here.
import json
from datetime import datetime, date, time
from django.http import HttpResponse
from .models import Temperature


time_format = '%H:%M:%S'
date_format = '%Y-%m-%d'


def basic_view(request):
    try:
        if request.method == 'POST':
            print request.POST
            request_data = json.loads(request.body)

            for record in request_data:
                t = Temperature(date=datetime.strptime(record['date'], date_format).date(),
                                time=datetime.strptime(record['time'], time_format).time(),
                                temperature=record['temp'])  # 01:12:33
                t.put()

            return HttpResponse(json.dumps(dict(success=True)), content_type='application/json')
        else:
            q = Temperature.query()
            q = q.order(-Temperature.date, -Temperature.time)
            results = q.fetch(100)
            results = map(lambda d: {'time': d.time.strftime(time_format), 'date': d.date.strftime(date_format),
                          'temp': d.temperature}, results)

            return HttpResponse(json.dumps(dict(success=True, data=results)), content_type='application/json')
    except Exception as e:
        return HttpResponse(json.dumps(dict(success=False, error=str(e))), content_type='application/json')


def test_view(request):
    return HttpResponse(request.body)
