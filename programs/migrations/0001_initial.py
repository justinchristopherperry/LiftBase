# Generated by Django 2.1.7 on 2019-06-19 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('sets', models.IntegerField(blank=True, null=True)),
                ('reps', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('rpe', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('program', models.CharField(max_length=50)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('lifts', models.ManyToManyField(blank=True, to='programs.Lift')),
            ],
        ),
    ]