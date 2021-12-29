from base.models import BaseModel

from django.db import models

from base.models import User
from .coin import Coin


class Alert(BaseModel):
    class Relations(models.TextChoices):
        INCREASES_BY = '>='
        DECREASES_BY = '<='
        EQUALS = '='

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=20, decimal_places=10)
    target_price = models.DecimalField(max_digits=20, decimal_places=10)
    relation = models.CharField(max_length=2, choices=Relations.choices, default=Relations.EQUALS)
    completed = models.BooleanField(default=False)

    @staticmethod
    def create_alert(data):
        id = None
        try:
            alert = Alert(**data)
            alert.save()
            id = alert.id
        except Exception as e:
            print(e)
        finally:
            return id

    def email_template(self):
        subject = f"{self.coin.name} just reached target price of {self.target_price}"
        body = f"Hey {self.user.first_name}!!. Your Alert for {self.coin.name} registered on {self.created_at} just reached the target price of {self.target_price}."
        return {'subject': subject, 'body': body}
