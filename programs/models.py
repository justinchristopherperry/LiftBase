from django.db import models

class Program(models.Model):
    username = models.CharField(max_length=25)
    program = models.CharField(max_length=50)
    version = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(blank=True, null=True)
    lifts = models.ManyToManyField('Lift', blank=True)

class Lift(models.Model):
    exercise = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    rpe = models.DecimalField(decimal_places=1, max_digits=2, blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.exercise

