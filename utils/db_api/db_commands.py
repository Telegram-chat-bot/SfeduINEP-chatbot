from django_admin.bot.models import Admission, About, Passing_scores, Directions, Num_places, Questions, Welcome_message, ProfTest
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
    return Directions.objects.values()

@sync_to_async
def get_faq():
    return Questions.objects.all().values_list("faq")[0][0]

@sync_to_async
def get_welcome_msg():
    return Welcome_message.objects.all().values_list("message")[0][0]

@sync_to_async
def get_questions(id):
    return ProfTest.objects.get(direction_id = id).question