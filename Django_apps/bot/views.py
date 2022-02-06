from django.shortcuts import render
from Django_apps.feedback.models import Feedback
from Django_apps.django_admin.settings import BASE_DIR
import os


# Create your views here.
def main_page(request):
    data = Feedback.objects.order_by("-created_at")
    context = {"response": data}
    return render(request, os.path.join(BASE_DIR, "templates/bot/index.html"), context)
