from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Program, Lift

def home(request):
    allPrograms = Program.objects.all()
    return render(request, 'home.html', {'allPrograms': allPrograms})

def program_detail(request, id):
    try:
        program = Program.objects.get(id=id)
    except Program.DoesNotExist:
        raise Http404('Program not found.')
    return render(request, 'program_detail.html', {'program': program})