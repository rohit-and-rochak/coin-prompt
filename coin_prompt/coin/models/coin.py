from decimal import Decimal
import requests

from base.models import BaseModel

from django.conf import settings
from django.db import models


class Coin(BaseModel):
    name = models.CharField(max_length=50)

    def get_price(self):
        endpoint = settings.WAZIRX_API_COIN.format(self.name.lower())
        response = requests.get(endpoint)
        price = {}
        if response.ok:
            result = response.json()
            price['price'] = Decimal(result['lastPrice'])

        return price

    @property
    def logo(self):
        return f'/images/icons/{self.name.lower()}.png'