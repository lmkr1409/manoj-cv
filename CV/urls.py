from django import views
from django.urls import path

from CV import views as cv_views

urlpatterns = [
    path('CV', cv_views.DisplayCV.as_view()),
    path('home', cv_views.MyProfile.as_view()),
]