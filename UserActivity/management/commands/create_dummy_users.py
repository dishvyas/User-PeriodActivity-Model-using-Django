from django.core.management.base import BaseCommand, CommandError
import django
django.setup()
from random import *
from faker import Faker
fake = Faker()
from django.apps import apps
User = apps.get_model('UserActivity', 'User')
ActivityPeriod = apps.get_model('UserActivity','ActivityPeriod')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')
    
    def handle(self, *args, **kwargs):    
        total = kwargs['total']
        for i in range(total):
            users = User.objects.create(user_id=fake.pystr(), real_name=fake.name(), tz=fake.timezone())

            for j in range(0, randint(0, total)):
                users.activity_periods.add(
                    ActivityPeriod.objects.create(start_time=fake.date_time(), end_time=fake.date_time()))

