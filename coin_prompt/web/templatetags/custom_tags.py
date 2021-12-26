from math import modf
from babel import numbers

from django import template

register = template.Library()


@register.filter(name="abs")
def absolute_value(value):
    return abs(float(value))


@register.filter
def inr(value):
    return numbers.format_currency(value, 'INR', decimal_quantization=False)


@register.filter
def strip_zero(value):
    fraction = modf(value)[0]
    if fraction != 0:
        return str(value).rstrip('0')
    else:
        return round(value, 2)


@register.filter
def get_coin_value(d, coin_name):
    coin = d.get(coin_name)
    if coin:
        return coin['price']
