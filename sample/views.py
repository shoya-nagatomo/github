from django.http import HttpResponse
from django.views import generic
from .models import Location, WeatherData
import logging


logger = logging.getLogger('development')


class IndexView(generic.ListView):
    model = Location
    paginate_by = 5
    ordering = ['-updated_at']
    template_name = 'sample/index.html'


class DetailView(generic.DetailView):
    model = Location
    template_name = 'sample/detail.html'


def exec_ajax(request, pk):

    if request.method == 'GET':  # GETの処理
        param1 = request.GET.get("param1")  # GETパラメータ1
        param2 = request.GET.get("param2")  # GETパラメータ2
        param3 = request.GET.get("param3")  # GETパラメータ3
        logger.debug(param1 + param2 + param3)
        return HttpResponse(param1 + param2 + param3)

    elif request.method == 'POST':  # POSTの処理
        data1 = request.POST.get("input_data")  # POSTで渡された値
        logger.debug(data1)
        return HttpResponse(data1)
