import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections


def index(request):
    context = {}
    return render(request, 'index/index.html', context)
