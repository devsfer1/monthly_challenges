from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
  return HttpResponse('Januaryy')

def index_february(request):
  return HttpResponse('Frebruary works')


def monthly_challenge_by_number(request, month):
  return HttpResponse(month)

def monthly_challenge(request, month):
  challenge_text = None
  if month == 'january':
    challenge_text = 'Eat no meat for the entire month'
  elif month == 'february':
    challenge_text = 'Walk for at least 20 minutes every day'
  elif month == 'march':
    challenge_text = 'Learn Django for at least 20 minutes every day'
  else:
    return HttpResponseNotFound('invalid path')
  return HttpResponse(challenge_text)
