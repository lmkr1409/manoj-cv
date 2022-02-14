from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views import View
import os

from resume.settings import BASE_DIR

# Create your views here.


class DisplayCV(View):

    def get(self, request):
        return FileResponse(open(os.path.join(BASE_DIR, 'static', 'CV', 'Resume_ManojKumar.pdf'), 'rb'), content_type='application/pdf')


class MyProfile(View):

    def get(self, request):
        return render(request, "home.html")