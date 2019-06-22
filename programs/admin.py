from django.contrib import admin
from .models import Program, Lift

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program', 'version', 'username']