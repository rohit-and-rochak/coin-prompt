from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST


from .models import Alert, Coin
from web.tasks import check_alert_trigger


@require_POST
@login_required
def create_alert(request):

    if request.is_ajax:
        data = request.POST
        user = request.user
        coin = Coin.objects.filter(name=data.get('coin')).first()

        if not coin:
            return JsonResponse({'error': f'Coin {data.get("coin")} not found'}, status=500)
        else:
            alert = {'user': user, 'coin': coin}
            alert['base_price'] = data.get('base_price')
            alert['target_price'] = data.get('target_price')
            alert['relation'] = data.get('relation')
            id = Alert.create_alert(alert)

            if not id:
                return JsonResponse({'error': 'There occurred an error while creating the alert'}, status=500)

            check_alert_trigger(id, repeat=10, repeat_until=None)

            return JsonResponse({'data': {}}, status=200)

    return JsonResponse({'error': 'Invalid Request'}, status=500)


@require_POST
@login_required
def delete_alert(request):
    if request.is_ajax:
        data = request.POST
        user = request.user
        alert = Alert.objects.filter(user=user, coin__name=data.get('coin')).first()
        if alert:
            alert.delete()
            return JsonResponse({'data': {}}, status=200)
        else:
            return JsonResponse({'error': f'Coin {data.get("coin")} not found'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=500)
