from decimal import Decimal
import locale
from babel import numbers

from django import template

register = template.Library()


@register.filter(name="abs")
def absolute_value(value):
    return abs(float(value))


@register.filter
def inr(value):
    return numbers.format_currency(value, 'INR', decimal_quantization=False)
