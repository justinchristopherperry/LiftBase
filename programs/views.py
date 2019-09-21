from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Program
from .forms import ProgramForm

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

    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/upload/thank_you/')
    else:
        form = ProgramForm()

    return render(request, 'upload.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

def contact(request):
    return render(request, 'contact.html')