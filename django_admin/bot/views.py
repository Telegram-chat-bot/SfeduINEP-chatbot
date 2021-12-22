from django.shortcuts import render
from django_admin.feedback.models import Feedback


# Create your views here.
def main_page(request):
    data = Feedback.objects
    context = {"response": data}
    return render(request, "bot/index.html", context)