from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext

from client.models import Genre


def show_genres(request):
    return render_to_response("genres.html",
                          {'nodes':Genre.objects.all()})
