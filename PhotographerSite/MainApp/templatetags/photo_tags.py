from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    """Форматирует значение как валюту"""
    try:
        value = float(value)
        return f"{value:,.2f} ₽".replace(',', ' ')
    except (ValueError, TypeError):
        return value