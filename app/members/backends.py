
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from config import settings

User = get_user_model()


class SettingsBackend:

    def authenticate(self, request, username=None, password=None):
        login_vaild = (settings.ADMIN_USERNAME == username)
        pwd_vaild = check_password(password, settings.ADMIN_PASSWORD)

        if login_vaild and pwd_vaild:
            try:
                user = User.objects.get(username=username)

            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()

            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None




