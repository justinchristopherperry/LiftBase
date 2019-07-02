from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Program

def home(request):
    all_programs = Program.objects.all()
    return render(request, 'home.html', {'all_programs': all_programs})

def program_detail(request, id):
    try:
        program = Program.objects.get(id=id)
    except Program.DoesNotExist:
        raise Http404('Program not found.')
    return render(request, 'program_detail.html', {'program': program})

def upload(request):
    testProgram = Program.objects.get(id=4)
    return render(request, 'program_detail.html', {'program': testProgram})