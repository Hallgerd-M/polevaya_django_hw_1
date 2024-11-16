from django.core.management import BaseCommand
from django.contrib.auth.models import Group

from users.models import User


class ModeratorCommand(BaseCommand):
    help = "Add users as moderator"

    def handle(self, *args, **kwargs):
        user, _ = User.objects.create(email="example@example.com")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True

        moderators = Group.objects.get(name="moderators")
        user.groups.add(moderators)

        user.save()
