from django import template

register = template.Library()


def calculate_delay(index):
    return index * 150

register.filter('calculate_delay', calculate_delay)
