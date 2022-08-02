from django import template
from django.conf import settings
import string
import random

register = template.Library()

@register.simple_tag
def get_version_random_file_static():
    return '?v=' + ''.join(random.choice(string.ascii_letters) for x in range(10))


@register.simple_tag
def dataHora_BR(dataTime):
    return dataTime.strftime("%d/%m/%Y %H:%M")


@register.filter(name='int_format')
def int_format(value, decimal_points=3, seperator=u'.'):
    value = str(value)
    if len(value) <= decimal_points:
        return value
    # say here we have value = '12345' and the default params above
    parts = []
    while value:
        parts.append(value[-decimal_points:])
        value = value[:-decimal_points]
    # now we should have parts = ['345', '12']
    parts.reverse()
    # and the return value should be u'12.345'
    return seperator.join(parts)