from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from programs.models import Program, Lift
from pytz import UTC


DATETIME_FORMAT = '%m/%Y'

LIFT_NAMES = [
    'Squat',
    'Bench Press',
    'Deadlift',
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the program data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from program_data.csv into our Program model"

    def handle(self, *args, **options):
        if Lift.objects.exists() or Program.objects.exists():
            print('Program data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating lifts.")
        for lift_name in LIFT_NAMES:
            lift = Lift(exercise=lift_name)
            lift.save()
        print("Loading program data.")
        for row in DictReader(open('./program_data.csv')):
            program = Program()
            program.username = row['Username']
            program.program = row['Program']
            program.version = row['Version']
            program.description = row['Description']
            raw_submission_date = row['Date']
            submission_date = UTC.localize(
                datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            program.date = submission_date
            program.save()
            raw_lift_names = row['Lifts']
            lift_names = [name for name in raw_lift_names.split(', ') if name]
            for lift_name in lift_names:
                lift = Lift.objects.get(exercise=lift_name)
                program.lifts.add(lift)
            program.save()
        print("Done.")
