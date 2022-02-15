from django.shortcuts import render
from django.views import View
from django.shortcuts import render

# Create your views here.

class TocView(View):

    def get(self, request):
        return render(request, 'PythonNotes/toc.html')

class BaseDoc(View):
    
    def get(self, request):
        return render(request, 'PythonNotes/base.html')



class ImpTopicsView(View):

    def get(self, request):
        return render(request, 'PythonNotes/ImportantTopics.html')



class DataTypesView(View):

    def get(self, request):
        return render(request, 'PythonNotes/DataTypes.html')