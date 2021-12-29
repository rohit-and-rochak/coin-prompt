import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def get_token(self):
        return str(Token.objects.get_or_create(user=self)[0])