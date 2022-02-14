from django.shortcuts import render
from django.views import View
from django.shortcuts import render
import markdown

import os
from resume.settings import BASE_DIR
# Create your views here.


class BaseDoc(View):
    
    def get(self, request):
        # base = markdown.markdown(open(os.path.join(BASE_DIR, "Projects", "Static", "PythonDoc", "base.md")).read())
        return render(request, 'PythonNotes/base.html')



class ImpTopicsView(View):

    def get(self, request):
        return render(request, 'PythonNotes/ImportantTopics.html')



class SequenceTypesView(View):

    def get(self, request):
        return render(request, 'PythonNotes/SequenceTypes.html')