from django.core.management.base import BaseCommand

from faker import Faker

from teachers.models import Teacher

fake = Faker()


class Command(BaseCommand):
    help = "Add teachers to database, default = 10 teachers or specify number by arg"

    def add_arguments(self, parser):
        parser.add_argument("number", nargs='?', type=int, default=100 )

    def handle(self, *args, **options):
        for i in range(options["number"]):
            teacher = Teacher.objects.create(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                birth_date = fake.date(),
                subject = fake.job()
            )

            self.stdout.write(
                self.style.SUCCESS('Successfully created teacher "%s"' % teacher.id)
            )