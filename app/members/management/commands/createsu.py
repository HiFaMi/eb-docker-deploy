
from django.core.management import BaseCommand, CommandError

from config import settings
from members.models import User


class Command(BaseCommand):
    help = 'Create super User'

    def handle(self, *args, **options):
        username = settings.base.SUPER_NAME
        password = settings.base.SUPER_PASSWORD
        email = None

        if User.objects.filter(username=username).exists():
            self.stderr.write(self.style.ERROR('This name already exists check username'))

        else:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )

            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
