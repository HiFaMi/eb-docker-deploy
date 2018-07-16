from django.core.management import BaseCommand, CommandError
from members.models import User


class Command(BaseCommand):
    help = 'Create super user!!'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            dest='username',
            required=True,
            help='superuser id',)

        parser.add_argument(
            '--password',
            dest='password',
            required=True,
            help='superuser password',
        )

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = None

        if User.objects.filter(username=username).exists():
            raise CommandError("This username is exists check user name")
        else:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
            )

            user.save()

            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))

