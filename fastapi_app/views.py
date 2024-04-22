from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def proxy_view(request):   
    response = requests.get("http://localhost:8000/mngadex/")

    return HttpResponse(response.text)    