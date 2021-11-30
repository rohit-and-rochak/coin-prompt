import requests
import locale

from django.shortcuts import render
from django.conf import settings

def home(request):
    endpoint = settings.WAZIRX_API_ALL
    response = requests.get(endpoint)
    coins = {}
    if response.ok:
        for coin in response.json():
            if coin['quoteAsset'] == 'inr':
                name = coin['baseAsset']
                change = round((float(coin['lastPrice']) - float(coin['openPrice'])) / float(coin['openPrice']), 3)
                price = coin['lastPrice']

                coins[name.upper()] = {'price': price, 'change': change, 'icon': 'images/icons/{}.png'.format(name)}

    return render(request, 'home.html', {'coins': coins, 'generic_icon': 'images/icons/generic.png'})
