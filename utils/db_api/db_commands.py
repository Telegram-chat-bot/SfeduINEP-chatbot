import asyncio
from django_admin.bot.models import *
from asgiref.sync import sync_to_async

#-----------------------------------------
#Получение данных для раздела Поступление
@sync_to_async
def get_admission_data():
    return Admission.objects.values()[0]

@sync_to_async
def get_admission_rules():
        return Admission.objects.values_list("admission_rules")[0]
    
@sync_to_async
def get_admission_submit_doc():
    return Admission.objects.values_list("submit_doc")[0]

#Получение данных для раздела Проходные баллы
@sync_to_async
def get_admission_passing_scores(id):
    return Passing_scores.objects.get(direction_id = id).inf

#Получение данных для раздела Количество мест
@sync_to_async
def get_admission_num_places(id):
    return Num_places.objects.get(direction_id = id).inf

@sync_to_async
def get_admission_achievements():
    return Admission.objects.values_list("achievements")[0]

@sync_to_async
def get_admission_spec_rights():
    return Admission.objects.values_list("special_rights")[0]

@sync_to_async
def get_admission_stat():
    return Admission.objects.values_list("admission_stat")[0]
    
@sync_to_async
def get_admission_enrollment_proc():
    return Admission.objects.values_list("enrollment_proc")[0]

#--------------------------------------------




#Получение данных для раздела Об институте
@sync_to_async
def get_about_data():
    return About.objects.values()

@sync_to_async
def get_about_acquaintance():
    return About.objects.values_list("acquaintance")[0]

@sync_to_async
def get_about_excursion():
    return About.objects.values_list("excursion")[0]

@sync_to_async
def get_about_science():
    return About.objects.values_list("science")[0]

@sync_to_async
def get_about_events():
    return About.objects.values_list("events")[0]

@sync_to_async
def get_about_partners_work():
    return About.objects.values_list("partners_work")[0]

@sync_to_async
def get_about_council():
    return About.objects.values_list("stud_council")[0]

@sync_to_async
def get_about_photo():
    return About.objects.values_list("photo")[0]

@sync_to_async
def get_about_contacts():
    return About.objects.values_list("contacts")[0]

#-------------------------------------------




#Получение данных о направлениях подготовки
@sync_to_async
def get_directions():
    return Directions.objects.values()

#Получение кода направлений
@sync_to_async
def get_dir_code():
    return Directions.objects.values("id", "direction")

#-------------------------------------------



#Получение данных для раздела FAQ
@sync_to_async
def get_faq():
    return Questions.objects.all().values_list("faq")[0][0]

#Получение приветственного сообщения
@sync_to_async
def get_welcome_msg():
    return Welcome_message.objects.all().values_list("message")[0][0]

#Получение ID чата для направления подготовки
@sync_to_async
def get_chat_id_group(code):
    origin_data = Directions.objects.get(direction=code).id
    return ChatID.objects.get(chat_direction_id = origin_data).chat_id

#Получение вопросов для проф.теста
@sync_to_async
def get_questions():
    directions_data = Directions.objects.values("id", "direction")
    questions_test = ProfTest.objects.values()

    result = {}
    for data in directions_data:
        for question in questions_test:
            if data["id"] == question["direction_id"]:
                result[data["direction"]] = question["question"].split("\n")
                
    return result
