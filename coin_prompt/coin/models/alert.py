from base.models import BaseModel

from django.db import models

from base.models import User
from .coin import Coin


class Alert(BaseModel):
    class Relations(models.TextChoices):
        LESS_THAN = '<'
        GREATER_THAN = '>'
        EQUALS = '='

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=20, decimal_places=10)
    target_price = models.DecimalField(max_digits=20, decimal_places=10)
    relation = models.CharField(max_length=1, choices=Relations.choices, default=Relations.EQUALS)
    completed = models.BooleanField(default=False)
