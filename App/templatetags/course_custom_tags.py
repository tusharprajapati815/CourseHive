from django import template
from App.models import UserCourse, Course
import math

register = template.Library()

# 100 -> 10% --> mrp - ( mrp * discount * 0.01) = sellprice

@register.simple_tag
def cal_sellprice(price, discount):
    if discount is None or discount is 0:
        return price
    
    sellprice = price
    sellprice = price - (price * discount * 0.01)
    return math.floor(sellprice)

@register.filter(name="currency")
def currency(price):
    return f'₹{price}'

@register.simple_tag
def is_enrolled(request, course):
    if not request.user.is_authenticated:
        return False
    
    user = request.user
    try:
        user_course = UserCourse.objects.get(user = user, course = course)
        return True
    except:
        return False

