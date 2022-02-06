from django.shortcuts import render
from django_admin.feedback.models import Feedback
import os


# Create your views here.
def main_page(request):
    data = Feedback.objects.order_by("-created_at")
    context = {"response": data}
    return render(request, "bot/index.html", context)