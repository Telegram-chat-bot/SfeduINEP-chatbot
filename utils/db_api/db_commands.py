from os import name
from django_admin.bot.models import Admission, About, Passing_scores, Directions, Num_places
from asgiref.sync import sync_to_async

@sync_to_async
def get_admission_data():
    return Admission.objects.values()

@sync_to_async
def get_about_data():
    return About.objects.values()


@sync_to_async
def get_passing_scores(id):
    return Passing_scores.objects.get(direction_id = id).inf

@sync_to_async
def get_num_places(id):
    return Num_places.objects.get(direction_id = id).inf

@sync_to_async
def get_directions():
    return Directions.objects.values("id", "level", "direction", "name_of_dir", "inf")

