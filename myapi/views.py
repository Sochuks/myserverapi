from django.shortcuts import render


# from rest_framework import generics
from .models import Details
# from .serializers import ServerapiSerializer
# Create your views here.

from rest_framework.decorators import api_view

from django.http import JsonResponse

@api_view(["GET"])
def home(request, *args, **kwargs):
  header = {"Access-Control-Allow-Origin":"*"}
  data = {
    "slackUsername":"sochuks_kajang",
    "backend":True,
    "age": 29,
    "bio":"Skilled & motivated Backend Developer"
  }
  return JsonResponse(data, headers=header)
