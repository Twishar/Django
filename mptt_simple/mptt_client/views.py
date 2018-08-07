from django.shortcuts import render

# Create your views here.
from mptt_client.models import Genre


def show_genres(request):
    return render(request, "mptt_client/genres.html", {'genres': Genre.objects.all()})
