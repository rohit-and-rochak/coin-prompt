from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST


from .models import Alert, Coin

@require_POST
@login_required
def create_alert(request):
    if request.is_ajax:
        data = request.POST
        user = request.user
        coin = Coin.objects.filter(name=data.get('coin')).first()
        if coin:
            alert = {'user': user, 'coin': coin}
            alert['base_price'] = data.get('base_price')
            alert['target_price'] = data.get('target_price')
            alert['relation'] = data.get('relation')
            Alert.create_alert(alert)

            return JsonResponse({'data': {}}, status=200)
        else:
            return JsonResponse({'error': f'Coin {data.get("coin")} not found'}, status=500)

    return JsonResponse({'error': 'Invalid Response'}, status=500)
