from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
    return HttpResponseNotFound('month not valid')

  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
  
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
      challenge_text = monthly_challenges[month]
      response_data = f"<h1>{challenge_text}</h1>"
      return HttpResponse(response_data)
  except:
      return HttpResponseNotFound('<h1>Month not supported</h1>')
