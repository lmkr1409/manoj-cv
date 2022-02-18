from django.urls import path

from Projects import views as pr_views

urlpatterns = [
    path('python_notes/toc', pr_views.TocView.as_view()),
    path('python_notes/base', pr_views.BaseDoc.as_view()),
    path('python_notes/important_topics', pr_views.ImpTopicsView.as_view()),
    path('python_notes/data_types', pr_views.DataTypesView.as_view()),
    path('python_notes/general_topics', pr_views.GeneralTopics.as_view()),
    path('python_notes/functions', pr_views.FunctionsView.as_view()),

]