from background_task import background

from coin.models import Alert
from .email_helper import Mail

@background
def check_alert_trigger(alert_id):
    alert = Alert.objects.filter(id=alert_id, completed=False).first()

    if alert:
        current_price = alert.coin.get_price()
        target_price = alert.target_price
        relation = alert.relation

        trigger = eval(f"{current_price} {relation} {target_price}")
        if trigger:
            alert.completed = True
            alert.save()
            mail = alert.email_template()
            Mail.send(mail['subject'], mail['message'], alert.user.email)
