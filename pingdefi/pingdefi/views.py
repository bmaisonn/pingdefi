from django.http import HttpResponse


def index(request):
    return HttpResponse("Play a game!")