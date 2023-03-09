from django import template

register = template.Library()


@register.filter('addCSSClass')
def addCSSClass(value, arg: str):
    return value.as_widget(attrs={'class': arg})