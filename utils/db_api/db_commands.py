from os import name
from django_admin.bot.models import Admission, About, Passing_scores, Directions, Num_places
from asgiref.sync import sync_to_async

@sync_to_async
def get_admission_data(*args):
    return Admission.objects.values_list(*args)

@sync_to_async
def get_about_data(*args):
    return About.objects.values_list(*args)


# @sync_to_async
# def get_passing_scores():
#     main = Directions.objects.get(pk = 4)
    
    
#     return Passing_scores.objects.get(direction__id = main.id)

@sync_to_async
def get_directions():
    return Directions.objects.values("level", "direction", "name_of_dir", "inf")

