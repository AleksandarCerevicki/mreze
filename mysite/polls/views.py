from django.http import HttpResponse


def index(request):
    return HttpResponse("Ja volim da igram igre")