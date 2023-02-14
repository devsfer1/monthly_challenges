from django.urls import path

from . import views

urlpatterns = [
  # path("january", views.index),
  # path("february", views.index_february),
  ##dynamic paths
  path('<int:month>', views.monthly_challenge_by_number),
  path('<str:month>', views.monthly_challenge)
]