from django.shortcuts import render
from feedback.models import Feedback
from django_admin.settings import BASE_DIR
import os


# Create your views here.
def main_page(request):
    data = Feedback.objects.order_by("-created_at")
    context = {"response": data}
    return render(request, os.path.join(BASE_DIR, "templates/bot/index.html"), context)
