
from django.urls import path

from CV import views as cv_views

urlpatterns = [
    path('', cv_views.MyProfile.as_view()),
    path('CV', cv_views.DisplayCV.as_view()),
]