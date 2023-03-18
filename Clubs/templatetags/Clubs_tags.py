# from django import template
# from Clubs.models import Schedule
#
# register = template.Library()
#
#
# @register.simple_tag
# def get_obj_attr(club, attr):
#
#     obj = Schedule.objects.get(club_id=club.id)
#     dayTable = getattr(obj, attr)
#     return sorted(dayTable.items())