from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(ChatIDAdmission)


@admin.register(ChatIDDirections)
class ChatIDAdmin(admin.ModelAdmin):
    list_display = ["chat_direction", "chat_id"]

# admin.site.register(ChatIDDirections)
