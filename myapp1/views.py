from django.shortcuts import render

from django.http import JsonResponse

def push_json(request):
    return JsonResponse({"Name": "Hello World!"})
# Create your views here.
