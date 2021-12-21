from django.contrib import admin
from .models import *

# admin.site.register(Feedback)
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["username", "date"]