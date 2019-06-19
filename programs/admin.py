from django.contrib import admin

from .models import Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program', 'version', 'username']