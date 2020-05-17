from django.http import HttpResponse
import datetime


def index(request):
    time_now = datetime.datetime.now()
    return HttpResponse("Hello, world. You're at the polls index. {}".format(time_now))

# Create your views here.
