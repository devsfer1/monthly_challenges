from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
  "january": "Eat no meat for the entire month",
  "february": "Walk for at least 20 minutes every day",
  "march": "Learn Django for at least 20 minutes every day",
  "april": "Eat no meat for the entire month",
  "may": "Meditate for at least 10 minutes every day",
  "june": "Read a book for at least 30 minutes every day",
  "july": "Take a photo every day and create a photo journal at the end of the month",
  "august": "Write a journal entry every day",
  "september": "Learn a new word every day and use it in conversation",
  "october": "Do a random act of kindness every day",
  "november": "Take a break from social media for the entire month",
  "december": "Do something creative every day, like drawing, painting or writing."
}

def index(request):
 return HttpResponse('Januaryy')

def index_february(request):
  return HttpResponse('Frebruary works')


def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
    return HttpResponseNotFound('month not valid')

  redirect_month = months[month - 1]
  
  return HttpResponseRedirect('/challenges/' + redirect_month)

def monthly_challenge(request, month):
  # print(request, month)
  try:
   challenge_text = monthly_challenges[month]
   return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound('Month not supported')

  # return HttpResponse(challenge_text)
