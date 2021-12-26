from django.shortcuts import render
from feedback.models import Feedback


# Create your views here.
def main_page(request):
    data = Feedback.objects.order_by("-created_at")
    context = {"response": data}
    return render(request, "bot/index.html", context)
