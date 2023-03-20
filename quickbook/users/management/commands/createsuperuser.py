from getpass import getpass
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        username = input('Enter username: ')
        password = getpass('Enter password: ')
        name = input('Enter name: ')
        email = input('Enter email: ')

        # Create the superuser with the provided information
        User.objects.create_superuser(username=username, password=password, name=name, email=email)

        self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
