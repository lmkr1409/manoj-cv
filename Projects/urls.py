from django.urls import path

from Projects import views as pr_views

urlpatterns = [
    path('python_notes/base.html', pr_views.BaseDoc.as_view()),
    path('python_notes/important_topics.html', pr_views.ImpTopicsView.as_view()),
    path('python_notes/sequence_types.html', pr_views.SequenceTypesView.as_view()),
]