import requests

from base.models import BaseModel

from django.conf import settings
from django.db import models


class Coin(BaseModel):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_price(coin):
        endpoint = settings.WAZIRX_API_COIN.format(coin)
        response = requests.get(endpoint)
        price = {}
        if response.ok:
            result = response.json()
            price['price'] = result['lastPrice']

        return price
