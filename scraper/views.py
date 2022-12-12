from django.shortcuts import render
from .models import Wine

def index(request):
    wine = Wine.objects.all().order_by("-cdate")
    return render(request, "index.html", {'wine':wine})
