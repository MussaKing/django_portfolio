from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


def main(request):
    return HttpResponse('main')

def chess_players(request):
    return HttpResponse('hr')

def pageNotFound(request, exception):
    return HttpResponseNotFound('Error page 404')