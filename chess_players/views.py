from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *


def main (request):
    return  HttpResponse('main')

def chess_players(request):
    return HttpResponse('hr')