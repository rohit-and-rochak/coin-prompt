import requests

from django.conf import settings
from django.shortcuts import render

from coin.models import Alert


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

    context = {'coins': coins}

    if request.user.is_authenticated:
        alerts = Alert.objects.filter(user=request.user)
        context['alerts'] = alerts

    return render(request, 'home.html', context)